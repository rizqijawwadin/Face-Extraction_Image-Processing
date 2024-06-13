# Face Extraction
This application focuses on building a facial feature extraction system using skin color segmentation methods. By leveraging OpenCV, the system simplifies the process of capturing facial data from large sample sets. The project aims to further develop facial recognition systems by implementing skin color segmentation, providing an efficient way to extract and analyze facial features.

### Dataset
you can get an example of the data that will be used in [Face Reg Base](http://www.face-reg.org/databases), or you can use it in the ```Aberdeen/``` directory file.

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
image = cv2.imread('C:/Users/Yeeeee/Desktop/Aberdeen/paul14.jpg') # change this part
```
#### Run the script
If you use Visual Studio Code, you can use ```F5```, or if you use the terminal you can run the following command :
```bash
python3 FaceExtraction.py
```

## Example Results
