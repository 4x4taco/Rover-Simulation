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

# Autonmous Navigation and Mapping
I relied on help from the Project Walkthrough video to structure my code and to understand the details of application.  I used the supplied files Perception.py, Drive_rover.py, supporting_functions and Desicion.py while adding another one, maneuver.py.  To clearly define how changes were made I will walk through each of the files and describe the sections that were added or modified.  

### Perception
A majority of the code used the Rover-Notebook was copied into the perception file.  This file was resposible for transoforming the stream of images to information that could detect navigable terrain and rocks.  The RGB values were set to 160 for the Red, Green and Blue channels.  An additional function was added to make the Rover act more autonomously.  This function was rover_stuck, and its purpose was to deterimine if the rover was stuck and to start a counter if this was the case.  When the counter was above a user set value a reverse was set to True and the rover would reverse until a speed on -1 m/s was reach at which point the Flage would be cleared.  The value to which to count was found by trial and error.  I also tried implementing a time function to do this for me but ulitmately it was more strain on the cpu than just using a simple +1 incrementer.  The find rocks function was also added to the perception file.  this file was a RGB filter set to 90,90,40 respectively.  This color Threshold did an excellent job of finding rocks.  An additional snippet of code was added on line 88.  The purpose of the code was to enable the rover to perform a 180 if it sensed it was at a dead end.  On line 187 a `rock_map.any` statement was used to detect rocks.  Once triggered the program would store rock information in the rover class.

### Desicion
This file was only modified slightly.  I added a bias of +-10 to line 28.  This kept the rover near the left side of the wall.  I did this to try and help the rover from overlappig areas that it had previously covered and try to raise the fidelity of the simulation. 

### Supporting Functions
I don't believe that I made any changes to this file.  Its purpose was to convert data for the unity enviroment, construct output images and manage communications.

### Manuever





