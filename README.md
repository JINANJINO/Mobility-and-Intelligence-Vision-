# Camera Parameter
The reason we need to learn Camera Parameters is to learn how 3D coordinates expressed in the World coordinate system are converted into 2D image coordinates through Camera Parameters.
In other words, it is a process of projecting coordinates in three dimensions into two dimensions.

## Homogeneous Coordinate
**Homogeneous Coordinates** are those that increase one dimension. For example, two dimensions are increased to three, and three dimensions are increased to four.

$$
\begin{pmatrix}
x \\
y
\end{pmatrix}
\\longmapsto\
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
$$

$$
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
\\longmapsto\
\begin{pmatrix}
x \\
y \\
z \\
1
\end{pmatrix}
$$

Homogeneous coordinates have three representative characteristics (actually there are more).

- Anything that is multiplied by a constant is treated the same.
  $$(λx,λy,λz)=(λx/λz,λy/λz,λz/λz)=(x/z,y/z,1)$$
- Translation can be expressed in matrix multiplication form.

$$
\textit{Euclidean coordinate:}\quad
\begin{pmatrix}
x \\
y
\end{pmatrix}
\longmapsto
\begin{cases}
x' = x + t_x \\
y' = y + t_y
\end{cases}
$$

$$
\textit{Homogeneous coordinate:}\quad
\begin{pmatrix}
x \\
y
\end{pmatrix}
\longmapsto
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
t_x & t_y & 1
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}
$$

- Infinite Point expression is possible.

$$
\textit{Homogeneous coordinates:}\quad
(x, y, w)^\top \sim (\lambda x, \lambda y, \lambda w)^\top,\ \lambda \neq 0
$$

$$
w \neq 0 \\Rightarrow\ \text{finite point in Euclidean space},\quad
(x_E, y_E) = \left(\frac{x}{w}, \frac{y}{w}\right)
$$

$$
w = 0 \\Rightarrow\ \text{point at infinity (ideal point)}
$$

$$
\text{Example: point at infinity in direction }(a,b)\quad
\begin{pmatrix}
a \\
b \\
0
\end{pmatrix}
$$

## Coordinate System of Camera
Before looking at the Camera Parameters, let's take a look at the actual Camera System.
<img width="1357" height="646" alt="image" src="https://github.com/user-attachments/assets/77f0a5be-3ff8-493f-a4de-9cb50c08a9f0" />

Looking at the figure above, there are three coordinate systems. The first is the **World Coordinate System**. This coordinate system is centered around any arbitrary point in the world.

The second is the **Camera Coordinate System**. This is a coordinate system that expresses any point in three dimensions as a coordinate system centered on the camera.The second is the Camera Coordinate System. This is a coordinate system that expresses any point in three dimensions as a coordinate system centered on the camera.

Lastly, there is the **image coordinate**. This is the coordinate system related to the projection of 3D coordinates captured by the camera into a 2D image.

What we are trying to do is to find out where a point in a 3D world coordinate system is mapped to a 2D image coordinate system.

$$
X_{\text{world}} \\rightarrow\ X_{\text{camera}} \\rightarrow\ X_{\text{image}}
$$

---
## Intrinsic Parameter
- **Pinhole Camera Model**
<img width="623" height="362" alt="image" src="https://github.com/user-attachments/assets/4fc217be-ab27-47d7-8c08-3741cbfda9de" />

The most basic model for describing a camera is the **pinhole camera model**. As shown above, light reflected from an object enters the camera through a small hole, creating an image inside the camera. Modern cameras can be thought of as focusing light through a lens (a small hole) and forming an image on the camera sensor.

<img width="623" height="362" alt="image" src="https://github.com/user-attachments/assets/8310176f-6409-4a56-bfde-ece73b0bfa1a" />

Here, $$X$$ is a 3D coordinate in any space, and the image plane is where the object is projected on the camera lens. **f** is the distance between the center of the camera and the image plane, which is called the **focal length**, and **Z** is the distance between the camera coordinate and the actual object, which is called the **Depth**.
What we want to know is where $$X$$ meets on the image plane. Therefore, we can utilize the **similarity property of triangles**, and express this in determinant form as follows.

$$
\begin{bmatrix}
x'\\
y'\\
z'
\end{bmatrix}
= \begin{bmatrix}
f & 0 & 0 & 0\\
0 & f & 0 & 0\\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z\\
1
\end{bmatrix}=
K [I\|0]X
$$

Previously, we assumed that the center of the image coordinate system was on the z-axis of the camera coordinate system. This assumption allowed the projected image coordinates to be calculated using a simple process utilizing the property of similarity. However, in modern CCD cameras, the center of the image coordinate system may not coincide with the camera coordinate system, depending on the location of the camera sensor.

<img width="623" height="362" alt="image" src="https://github.com/user-attachments/assets/2953b8de-8f6b-470d-86c2-7f4eff884d88" />

The figure above shows a case where the image coordinate system is translated and does not match the camera coordinate system. The image coordinate system may be rotated, but in most cases, it is only translated as shown above, so this article only assumes this case. This **translation of the image coordinate system** is equivalent to **translating the result of basic projection by the amount $(p_x, p_y)$** that the image coordinate system has moved.

$$
\begin{bmatrix}
x' \\
y' \\
z'
\end{bmatrix}=
\begin{bmatrix}
f & 0 & p_x \\
0 & f & p_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
= K [I \mid 0] X
$$

The intrinsic parameters referred to here are **$$f$$** and **$$(p_x, p_y)$$**.

---
## Extrinsic Parameter
**Extrinsic parameters** are parameters that determine where the camera is located in the world coordinates. In other words, they are parameters related to the camera pose, such as the coordinates where the camera is located and the degree of rotation.
<img width="510" height="309" alt="image" src="https://github.com/user-attachments/assets/f27f5da1-12e8-4edb-962b-f2a70bcbcb56" />

First, multiply the **translation matrix** to align the center of the World Coordinate and the center of the Camera Coordinate, and then use the **rotation matrix** to align the direction the Camera is looking.

$$
\begin{bmatrix}
x_{\text{camera}} \\
y_{\text{camera}} \\
z_{\text{camera}} \\
1
\end{bmatrix}=
\underbrace{
\begin{bmatrix}
R & 0 \\
0 & 1
\end{bmatrix}
}_{\textit{rotation}}
\underbrace{
\begin{bmatrix}
I & -C \\
0 & 1
\end{bmatrix}
}_{\textit{translation}}
\begin{bmatrix}
x_{\text{world}} \\
y_{\text{world}} \\
z_{\text{world}} \\
1
\end{bmatrix}=
\begin{bmatrix}
R & -RC \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
x_{\text{world}} \\
y_{\text{world}} \\
z_{\text{world}} \\
1
\end{bmatrix}
$$

Finally, we can combine these Intrinsic and Extrinsic Parameters to translate a point in the World coordinate system into the Image coordinate system.

---
## Back Projection

Above, we discussed camera parameters. This raises the question: If we know the camera's projection matrix, can't we reconstruct a 3D image from a 2D image by finding its inverse?
However, this is impossible. As seen in the figure of a pinhole camera, light reflected from an object and entering the pinhole travels in a straight line, and points along that line are projected onto the same pixel. Therefore, even if we reverse the projection process, we cannot find the original three-dimensional point. Therefore, **depth information** is required to accurately reconstruct the three-dimensional point.

The example below performs a back-projection task using a given image and intrinsic parameters. This demonstrates the role of intrinsic parameters.

**RGB Image**  
<img src="https://github.com/user-attachments/assets/f7491472-2be6-4c06-9997-087647a1f2d9" width="480" />

**Depth Image**  
<img src="https://github.com/user-attachments/assets/9a5ba22d-4f9d-4d5e-abc2-4285c228c0ee" width="480" />

**Back Projection**  
<img src="https://github.com/user-attachments/assets/fd4a85ff-2cdd-4959-a9ae-1e4a3a49a9d8" width="480" />

---

# Local Feature Matching
**Local Feature Matching** is a technology that matches points that are characteristic of objects within an image.
First, in order to perform Local Feature matching, we need to know two concepts.

> **KeyPoint** : It refers to a characteristic location that is distinguished from other points in a given image.(Ex: Corner, Edge)

> **Descripter** : It's easy to think of it as assigning an ID to a Keypoint, which serves to describe the characteristics of a specific point.

Image Matching is a method in which, when two images are given as input, a feature point is found, and the Descriptor assigns an ID to the feature point, and the same point is found in the two images using the keypoint and ID.
Using this technology, it is possible to find specific objects in a given image through image matching, and it is also possible to find the current location by looking at pre-collected image data through visual localization.
In addition to these, panoramic video shooting is also possible. This means that keypoint matching is used to search for identical points in two photos and stitch the two images together so that the found identical points overlap.

---
## Harris Coner Detector
**Harris Corner Detector** is a representative keypoint detector and is one of the methods for detecting corners based on the gradient method.
<img width="1740" height="780" alt="image" src="https://github.com/user-attachments/assets/4d714d40-c3ad-4c4c-8804-476ee62a6236" />

The characteristics of Corner are as follows. First, if you look at a **flat** picture, the pixel value does not change even if you move the window left and right.
For **Edge**, moving left and right results in a large change in pixel values, but moving vertically results in no change in pixel values. In other words, the amount of pixel change in only one direction is large.
Finally, let's consider corners. A **corner** is defined as an image whose pixel values ​​are large in all directions. Therefore, if we measure the change in pixel values ​​at a point on an image and the magnitude is large in all directions, we can determine that this is a corner.

---
## FAST(Features from Accelerated Segment Test)
The **FAST** algorithm is designed to increase speed. To briefly explain its principle, it recognizes a point as a corner if it differs from the surrounding pixels.

<img width="319" height="158" alt="image" src="https://github.com/user-attachments/assets/7bf90b4c-d3c1-4886-8b5d-3d2d7af981a9" />

- Target one pixel. 
- Gets 16 pixels surrounding the target.
- Pixel values ​​are compared by intensity. If the difference between pixels exceeds a predetermined threshold, it is recognized as a corner.

---

## SIFT
The **SIFT** algorithm is an algorithm that includes both keypoints and descriptors. The Harris Corner detector we looked at previously is rotation-invariant (it recognizes keypoints even when rotated). That is, it detects corners when the amount of pixel change is large by comparing in various directions, so it detects well even when rotated.

<img width="1268" height="340" alt="image" src="https://github.com/user-attachments/assets/824e4708-a62b-4a33-9009-f83afcd7f90d" />

However, the Harris Corner algorithm is not invariant to scale. That is, the image on the left below is recognized as a **corner**, but if the scale changes, it is recognized as an **edge**, as shown on the right.

<img width="1530" height="536" alt="image" src="https://github.com/user-attachments/assets/2367356d-c6f5-4e79-9509-0b53ce24373b" />


The **SIFT** algorithm can also address this scale invariance.
The **SIFT** algorithm provides a **keypoint detector** with scale invariance and a **descriptor** for matching each keypoint. (The Harris Corner detector and FAST algorithm do not have a detector.)
Let's first look at the detection process. To address the scale issue, multiple scaled images are created. Then, each scale is compared and combined to determine whether a given point is a keypoint.

<img width="740" height="549" alt="image" src="https://github.com/user-attachments/assets/402debc7-3203-4932-a015-6caf7988fcdd" />

Afterwards, a Gaussian filter is applied to the original image. This is because, when applied in this way, only the peak point survives, and the average point disappears.
That is, **Corners** and **Edges** become easier to find.
Afterwards, if you measure the pixel change through **Extream Detection**, you can see the point where it becomes Extrema.
<img width="1357" height="629" alt="image" src="https://github.com/user-attachments/assets/8d802372-7102-40d8-ab8a-a9affe5c3a9e" />

This time, let's look at the task for the descriptor in the SIFT algorithm. This is very similar to the Histogram of Gradient (HoG) method. First, the gradient for the surrounding pixels is calculated.

Afterwards, it is stacked as a histogram and used as a descriptor. The surrounding 16*16 pixels are divided into 4*4 cells and 8qkdgiddp eogks gradient histograms are created in each cell.
## Visual Localization

**Original Images**  
<img src="https://github.com/user-attachments/assets/8dbc631a-edca-4f9a-bb98-9a9bc2fc7dbe" width="360" />  
<img src="https://github.com/user-attachments/assets/dd1410c0-2fc2-4374-86db-135f6e0e2cee" width="360" />

**Local Feature Matching Result**  
<img src="https://github.com/user-attachments/assets/cc66a161-4a8c-40f2-bf43-a06c2ebd1bf0" width="720" />

---

## Using Panoramic Photos

**Original Images**  
<img src="https://github.com/user-attachments/assets/51949719-b5da-4af4-91bd-1c39d062421d" width="240" />  
<img src="https://github.com/user-attachments/assets/50149f7f-a0b9-48bc-8551-7f9ca8c72baf" width="240" />  
<img src="https://github.com/user-attachments/assets/381d8e71-fe82-4834-b091-a682a43a5d14" width="240" />

**Panorama**  
<img src="https://github.com/user-attachments/assets/a10aa048-188c-4b32-ac2b-0e148ceec928" width="720" />

---

# Depth

**Stereo Camera Left Image**  
<img src="https://github.com/user-attachments/assets/b0b7cc9a-ffc1-44bc-be23-e1e34ee62dca" width="360" />

**Stereo Camera Right Image**  
<img src="https://github.com/user-attachments/assets/f890b440-bb0d-4a67-acfd-1c8181339db3" width="360" />

**Depth Image (Disparity)**  
<img src="https://github.com/user-attachments/assets/260934f5-85c0-4b94-9920-056e5939d856" width="360" />
