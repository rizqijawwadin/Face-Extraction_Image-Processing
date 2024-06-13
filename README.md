# Face Extraction
This application focuses on building a facial feature extraction system using skin color segmentation methods. By leveraging OpenCV, the system simplifies the process of capturing facial data from large sample sets. The project aims to further develop facial recognition systems by implementing skin color segmentation, providing an efficient way to extract and analyze facial features.

### Dataset
You can get an example of the data that will be used in [Face Reg Base](http://www.face-reg.org/databases), or you can use it in the ```Aberdeen/``` directory file.

### Requirements
- Python ^3.x
- NumPy Library
- OpenCV Library

### Contributor
1. Mohamad Ferdy Alviansyah (22051204056)
2. Rizqi Jawwadin (22051204078)
3. Annanda Kurniawan (22051204083)
4. Henokh Wangsa Winidi (22051204084)

## Installation
#### Clone the repository
```bash
git clone https://github.com/rizqijawwadin/Face-Extraction_Image-Processing.git
```
#### Move to the directory
If you use Visual Studio Code, you can follow these steps
```bash
cd Face-Extraction_Image-Processing/
code .
```
#### Install library OpenCV
install the library first, you can type this in the terminal
```bash
pip install numpy opencv-python
```

## Usage
#### Preparing
Change the address of the image file you want to extract
```py
image = cv2.imread('C:/Users/Yee/Desktop/Aberdeen/paul14.jpg') # change this part
```
#### Configuration
change the iteration in the following section to find the best result
```py
# erode
skin_mask = cv2.erode(skin_mask, kernel, iterations=2) # change this part to erode
# dilate
skin_mask = cv2.dilate(skin_mask, kernel, iterations=2) # change this part to dilate
```
#### Run the script
If you use Visual Studio Code, you can use ```F5```, or if you use the terminal you can run the following command :
```bash
python3 FaceExtraction.py
```

## Example Results
The first step involves converting the image color model from RGB to HSV :
<div align="center">
  <img src="example result/Screenshot 2024-06-11%20160242.png" height="275">
  <img src="example result/Screenshot 2024-06-13%20140223.png" height="275">
  <img src="example result/Screenshot 2024-06-13%20140508.png" height="275">
</div>
The second step involves processing the image using the thresholding method to separate facial features from other objects based on differences in brightness levels using the HSV value :
<div align="center">
  <img src="example result/Screenshot 2024-06-11 160259.png" height="275">
  <img src="example result/Screenshot 2024-06-13 141022.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140638.png" height="275">
</div>
The third step involves processing the thresholded image morphologically using the Erode function to eliminate small noise generated during the thresholding stage :
<div align="center">
  <img src="example result/Screenshot 2024-06-11 160311.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140245.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140704.png" height="275">
</div>
The fourth step involves processing the eroded image to thicken certain objects :
<div align="center">
  <img src="example result/Screenshot 2024-06-11 160322.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140343.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140744.png" height="275">
</div>
The fifth step involves processing the dilated image using Gaussian Blur to fill in the remaining small gaps :
<div align="center">
  <img src="example result/Screenshot 2024-06-11 160343.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140403.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140819.png" height="275">
</div>
The final step involves using the extracted features from the previous stages to create a mask, resulting in a visual output that only includes the areas within the mask :
<div align="center">
  <img src="example result/Screenshot 2024-06-11 160351.png" height="275">
  <img src="example result/Screenshot 2024-06-13 135954.png" height="275">
  <img src="example result/Screenshot 2024-06-13 140910.png" height="275">
</div>
