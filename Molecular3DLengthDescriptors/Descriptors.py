def checklengthsordered(lengths):
    if lengths[0]<lengths[1]<lengths[2]:
        return True
    else:
        return False
    
def orderlengths(length_list):
    sorted_list = length_list.copy()
    sorted_list.sort()
    return sorted_list

def Flatness(lengths):
    """
    This is the shortest length. Units are the same as the coordinates. 
    """
    return lengths[0]
 
def Cubeularity(lengths):
    """
    A measure of how cubic a molecule is. 
    
    With 1 being a perfect cube.  
    
    Cubeularity = (Shortest*Medium*Longest)/(Longest)**3
    """
    return (lengths[0]*lengths[1]*lengths[2])/(lengths[2]**3)

def Plateularity(lengths):
    """
    A measure of how plate-like the molecule is. 
    
    Larger the output the more 2D plate-like the molecule is.
    
    Plateularity = (Medium*Longest)/ Shortest
    """
    return (lengths[1]*lengths[2])/(lengths[0])

def ShortOverLong(lengths):
    """
    A measure of how cubic a molecules is.
    
    0 means either a needle or plate shape.
    1 means perfect cube
    
    ShortOverLong = Shortest / Longest
    """
    return lengths[0]/lengths[2]

def MediumOverLong(lengths):
    """
    A measure of how needle or how plate-like a molecules is.
    
    0 means perfect needle shape
    1 means perfect plate-like shape
    
    ShortOverLong = Medium / Longest
    """
    return lengths[1]/lengths[2]

def CalcAllDesc(lengths):
    """
    Flattness => Shortest length
        Measure of how flat a molecules is.
    
    Cubularity => (Shortest*Medium*Longest)/(Longest)**3
        1 is a perfect cube. 
    
    Plateularity => (Medium*Longest)/ Shortest
        Larger value, more 2D plate-like.
        
    ShortOverLong => Shortest / Longest
        1 is perfect cube, 0 is needle or plate-like
        
    MediumOverLong => Medium / Longest
        1 is perfect plate-like shape, 0 is perfect needle shape       
    """
    
    if checklengthsordered(lengths):
        return {
            "Flattness":Flatness(lengths),
            "Cubeularity":Cubeularity(lengths),
            "Plateularity":Plateularity(lengths),
            "ShortOverLong":ShortOverLong(lengths),
            "MediumOverLong":MediumOverLong(lengths),
        }
    else:
        lengths = orderlengths(lengths)
        return {
            "Flattness":Flatness(lengths),
            "Cubeularity":Cubeularity(lengths),
            "Plateularity":Plateularity(lengths),
            "ShortOverLong":ShortOverLong(lengths),
            "MediumOverLong":MediumOverLong(lengths),
        } 

