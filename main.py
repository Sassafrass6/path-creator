from path_creator import make_path

# Resolution for the path. Higher number => more points
resolution = 8

# Path string. - for continuous path, | for broken path
path = 'G-X|Y-G-Z|R-G-T|U-G-V'
print(path)

# Mapping of symbol to 3d point position
points = { 'G' : [0,0,0],
           'X' : [1/2,0,0],
           'Y' : [0,1/2,0],
           'Z' : [0,0,1/2],
           'R' : [1/2,1/2,1/2],
           'T' : [0,1/2,1/2],
           'U' : [1/2,0,1/2],
           'V' : [1/2,1/2,0] }

# Create the interpolated path
fpath = make_path(path, points, resolution=resolution)

# Print the path string and the corresponding symmetry point indices 
print(path)
print(fpath['indices'])

# Print the path in the QE format
print(len(fpath['path']))
for j,f in enumerate(fpath['path']):
  #print(f'{j}'+'  %f %f %f 1'%tuple(f[i] for i in range(3)))
  print('  %f %f %f 1'%tuple(f[i] for i in range(3)))

