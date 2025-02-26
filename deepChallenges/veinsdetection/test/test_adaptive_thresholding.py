"""this module tests the adaptive thresholding class"""
from modules.vein_detection import VeinDetection
import cv2

# WARNING: Any big changes in the algorithm will result in a failed test
# in this case you will need to create a new pre-processed image in order for the test to pass
# Load the pre-processed  image
test_image_adaptive_thresholding = cv2.imread('img/test_image_adaptive_thresholding.png')

# The base image on which the tests will run on
base_image = cv2.imread('img/test_image.png')

# The base image gets grayscaled because adaptive thresholding needs a gray image
base_image_grayscaled = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)

# Call the constructor
vein_detection_class = VeinDetection(0)

# Call the adaptive thresholding function to create a thresholded image
image_adaptive_thresholding = vein_detection_class.adaptive_thresholding(base_image_grayscaled)

# Create histogram for both images
histo_test_adaptive_thresholding = cv2.calcHist([test_image_adaptive_thresholding], [0], None, [256], [0, 256])
histo_adaptive_thresholding = cv2.calcHist([image_adaptive_thresholding], [0], None, [256], [0, 256])


def test_height():
    """this test asserts that the height of both images are equal"""
    test_shape = test_image_adaptive_thresholding.shape
    shape = image_adaptive_thresholding.shape
    assert test_shape[0] == shape[0]


def test_width():
    """this test asserts that the width of both images are equal"""
    test_shape = test_image_adaptive_thresholding.shape
    shape = image_adaptive_thresholding.shape
    assert test_shape[1] == shape[1]


def test_histogram_length():
    """this test asserts that the histogram sizes of both images are equal"""
    assert len(histo_test_adaptive_thresholding) == len(histo_adaptive_thresholding)


def test_histogram_values():
    """this test asserts that the histogram values of both images are equal"""
    for gray_value in range(len(histo_adaptive_thresholding)):
        assert histo_test_adaptive_thresholding[gray_value] == histo_adaptive_thresholding[gray_value]
