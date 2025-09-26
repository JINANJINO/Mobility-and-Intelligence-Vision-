import json
import numpy as np
import cv2
import open3d as o3d

# 1) Load RGB-D images
rgb_bgr = cv2.imread("./rgb.png", cv2.IMREAD_COLOR)
depth_u16 = cv2.imread("./depth.png", cv2.IMREAD_UNCHANGED)   # uint16

# 2) mm -> m, 유효 픽셀 마스크
Z = depth_u16.astype(np.float32) / 1000.0
mask = depth_u16 > 0

h, w = depth_u16.shape
u = np.arange(w)
v = np.arange(h)
uu, vv = np.meshgrid(u, v)

# 3) camera parameters
fx = 525.0  # focal length x
fy = 525.0  # focal length y
cx = 319.5  # optical center x
cy = 239.5  # optical center y

# 4) back-projection

X = (uu - cx) * Z / fx
Y = (vv - cy) * Z / fy

# 5) visualization
pts = np.stack([X[mask], Y[mask], Z[mask]], 1)
colors = cv2.cvtColor(rgb_bgr, cv2.COLOR_BGR2RGB).reshape(-1,3)[mask.reshape(-1)]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pts)
pcd.colors = o3d.utility.Vector3dVector((colors/255.0).astype(np.float32))
o3d.visualization.draw_geometries([pcd], window_name="Manual Back-Projection")