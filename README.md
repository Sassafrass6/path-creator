# path-creator
Short code to create interpolated paths between predetermined 3-vectors. See main.py for example usage.  
  
Usage:  
(1) Import the function make_path from file path_creator.  
(2) Setup the path string and dictionary with mapping of point symbols to 3d positions.  
(3) Call the make_path function.  

  Arguments:  
    path (str): A string with delimiter separated high symmetry points.  
                Delimiter - specifies continuous path and | specifies a broken path  
    points (dict): Dictionary mapping high symmetry symbol to 3d k-position  
    resolution (float): Resolution of the k-path. Higher resolution means more points along each path line  
  
  Returns:  
    (dict): Dictionary with two keys 'path' and 'indices', specifying the 3d k-points of the path and the indices of high symmetry points, respectively.  

