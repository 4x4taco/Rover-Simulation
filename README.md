# Search and Sample Return Project


# Introduction
The purpose of this project is to program a virtual rover operating in a virtual unity environment supplied by Udacity.  The goal is  to map out the environment and locate rock samples while recording their location.  An additional requirement to this project is to pickup the samples and return them to the starting point in the map while optimizing the fidelity of the terrain mapped within the environment.  I choose to pick up the rock as my rover navigated the environment. 

## Notebook Analysis
###Perspect Transform
The first major compnent of the Rover-Notebook analyzed was the Perspective Transform.  The transform relied on pre-built functions from Open CV modules.  The purpose of this function was to take a 1st person perspective view and transformt the coordinates to use a top down view of the landsacpe.  

### Color Thresholding
The Color Thresholding function is meant to convert the output of the Perspective Transform to a black and white image highlighting the navigabel terrain in front of the rover.  The Color Thresholding function performs this action by applying a user set RGB color calue to each pixel in the array.  The array produced from this action is a truth array, setting the value to 1 everywhere there a true exists renders a black and white image of the navigable terrain.  A seperate Color Threshold function was written to find rocks.  This relies on the same process as before but with different filter settings.  The settings were configured to find only the yellow rocks.  This was accomplished using the interactive version of matplotlib and hovering over the ground rocs exracting the rgb information.

### Additional Color Thresholding
Two additional Color Thresholding functions were written to find rocks and obstacles.  The Find rocks function relies on the same process as before but with different filter settings.  The settings were configured to find only the yellow rocks.  This was accomplished using the interactive version of matplotlib and hovering over the ground rocs exracting the rgb information.  The other color thresholding function used was constructed using functions from Open CV.  The image was converted to HSV and the color of interest were also converted to HSV.  Applying the `cv2.inRange` and `cv2.bitwise_and` functions the brown color of the obstacles was extracted but the masked image contained alot of noise and black areas due to the non-homegenous properties of the terrain.  I decided to not incorporate this function into the rover controller because I was able to make the navigation work good enough using only navigable terrain.  

### Coordinate Transformations
Using the output from the Perspect Transform to obtain a top down view of the terrain and the Color Thresholding function to return a black and white picture the coordinate transformations can take place transforming the picture into world coordinates.  5 different functions were used to transform the screenshots into world coordinates.  In order they follow as:  rover_coords, to_polar_coords, rotate_pix, translate_pix, pix_to_world.  The purpose of rover_coords extracts the pixel coordinates from the screen shots.  To_polar-coords applies SRSS process to the pixel coordinates and extract the polar coordinates.  A translation and rotation are needed to apply the pixel coordinates to rover_coords.  The pix_to_world then applies the translatio and rotation to the pixel coordinates.  A mean avaerage is applied to the information and this is later used as steering input to guide the rover throught the environment.

### Process Image
A function was created that combined all of the previous functions into a single function that could take a picture as an input and apply a transform, threshold, and coordinate transformation all at once.  

### Movie py
A module called movie.py was used to string together a set of images inported from a .csv file.  The images had been processed by the Process_Image function and are played out to test the code before trying to connect to the unity environment.   

