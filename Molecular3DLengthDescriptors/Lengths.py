try:
    from rdkit import Chem
    from rdkit.Chem import AllChem
    import numpy as np
except ImportError:
    raise ImportError(
        "In order to run the `Molecular3DLengthDescriptors` module you must have the libraries: " +
        "`numpy` and `rdkit` installed.")


def GetLengthsRMSD(real_lengths,computed_lengths):
    squared_dev = [(real_len - compute_len)**2 for real_len, compute_len in zip(real_lengths, computed_lengths)]
    return np.sqrt(np.mean(squared_dev))

def GetLengthsFromCoords(coord_arr):
    def OrderLengths(length_list):
        sorted_list = length_list.copy()
        sorted_list.sort()
        return sorted_list
    evals, evecs = np.linalg.eig(np.cov(coord_arr, rowvar=False))
    return list(OrderLengths(np.sqrt(evals)))

class ComputeCoordsFrom2D:
    def __init__(self,numConfs=30,maxIter=600,numThreads =-1,pruneRmsThresh=0.5,nonBondedThresh=100.0):
        
        self.numconfs = numConfs
        self.maxiter = maxIter
        self.numthreads = numThreads
        self.prunermsthresh = pruneRmsThresh
        self.nonbondedthresh = nonBondedThresh
    
    def GetCoords(self,mol):
        """
        This outputs the 3D coords of the low energy conformer. 

        This function does the following:
        1. Conformers are generated
        2. Conformers are individually optimised MMFF94
        3. If MMFF94 fails, UFF is used. 
        4. Conformers are then pruned to remove duplicated and conformers which have the wrong symmetry
        5. Conformer coordinates are then calculated
        """

        molecule = Chem.AddHs(mol) # You get more accurate results with optimising energies when including Hs
        conformerIntegers = []
        conformers = Chem.AllChem.EmbedMultipleConfs(
            molecule,self.numconfs,pruneRmsThresh=self.prunermsthresh,numThreads =self.numthreads)

        #Using MMFF as it is more accurate than UFF. UFF fails less.
        try:
            optimised_and_energies = Chem.AllChem.MMFFOptimizeMoleculeConfs(
                molecule , maxIters=self.maxiter, numThreads =self.numthreads, nonBondedThresh =self.nonbondedthresh)
        except:
            try:
                optimised_and_energies = Chem.rdForceFieldHelpers.UFFOptimizeMoleculeConfs(
                    molecule , maxIters=self.maxiter, numThreads =self.numthreads)
            except ValueError:
                raise ValueError("Issue with input molecule. Both MMFF94 and UFF failed to optimise. This can occur in strange molecules which are very flexible or very rigid")

        EnergyDictionaryWithIDAsKey = {}
        FinalConformersToUse = {}

        #selection of only optimised conformers
        for conformer in conformers :
            optimised , energy = optimised_and_energies[conformer] 
            if optimised == 0:
                EnergyDictionaryWithIDAsKey [ conformer ] = energy 
                conformerIntegers.append(conformer)

        #Including the lowest energy conformer within the list
        lowestenergy = min( EnergyDictionaryWithIDAsKey.values () ) #lowest E conformer
        for k, v in (EnergyDictionaryWithIDAsKey.items()): 
            if v == lowestenergy:
                lowestEnergyConformerID = k
        molecule = AllChem.RemoveHs(molecule)

        return molecule.GetConformers()[lowestEnergyConformerID].GetPositions()
