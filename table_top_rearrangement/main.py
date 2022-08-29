import numpy as np
import matplotlib
import open3d as o3d


print("Testing open3d mesh Import Util")
mesh = o3d.io.read_triangle_mesh("data/Q1/boat.obj")
print(mesh)
o3d.io.write_triangle_mesh("results/Q1/triangle_meshes/copy_of_boat.ply",mesh)  
pcd = mesh.sample_points_poisson_disk(1000, 100, None)
    
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])