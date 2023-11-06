

def make_path ( path, points, resolution=8):
  '''
  Create a k-point path between high symmetry points.

  Arguments:
    path (str): A string with delimiter separated high symmetry points.
                Delimiter - specifies continuous path and | specifies a broken path
    points (dict): Dictionary mapping high symmetry symbol to 3d k-position
    resolution (float): Resolution of the k-path. Higher resolution means more points along each path line

  Returns:
    (dict): Dictionary with two keys 'path' and 'indices', specifying the 3d k-points of the path and the indices of high symmetry points, respectively.
  '''
  import numpy as np
  import re

  # Ensure points are numpy arrays
  for k,v in points.items():
    points[k] = np.array(v)

  # Break path on delimiters
  ps = re.split('-|\|', path)

  # Determine delimiters
  delim = path
  for p in ps:
    delim = delim.replace(p, '')

  # Make the path
  fpstr = '[0,'
  fpath = []
  for i,p in enumerate(ps[:-1]):
    p2 = ps[i+1]
    d = delim[i]

    pnt1 = points[p]
    pnt2 = points[p2]

    # Continuous path between points
    if d == '-':
      vec = pnt2-pnt1
      pres = int(np.round(2*resolution*np.linalg.norm(vec)))

      tpath = []
      sind = 0 if i==0 else 1
      for ip in np.linspace(0, 1, pres)[sind:]:
        tpath.append(pnt1 + ip*vec)

      fpath += tpath
      fpstr += str(len(fpath)-1) + ','

    # Broken segment between points
    elif d == '|':
      fpath += [pnt2]
      fpstr += str(len(fpath)-1) + ','

    else:
      raise ValueError(f'Invalid delimiter: {d}')

  fpath = np.array(fpath)
  fpstr = fpstr[:-1] + ']'

  return {'path':fpath, 'indices':fpstr}
