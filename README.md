# Search and Sample Return Project


# Introduction
The purpose of this project is to edit a program to control a virtual rover operating in a virtual unity environment, supplied by Udacity. The goal is to map out the environment and locate rock samples while recording their location. An additional requirement to this project is to pick up the samples and return them to the starting point in the map while optimizing the fidelity of the terrain mapped within the environment.  I choose to pick up the rock as my rover navigated the environment.  I did not program instructions for the return to the starting point to drop off the rocks.

## Notebook Analysis
### Perspect Transform
The first major component of the Rover-Notebook analyzed was the Perspective Transform. The transform relied on pre-built functions from Open CV library. The purpose of this function was to take a 1st person perspective view and transform the coordinates to a top down view of the landscape.
![Perspective Transform](perspective%20transform.png)

### Color Thresholding
The Color Thresholding function is meant to convert the output of the Perspective Transform to a black and white image highlighting the navigable terrain in front of the rover. The Color Thresholding function performs this action by applying a user set RGB color value to each pixel in the array. The array produced from this action is a truth array, setting the value to 1 everywhere there a true exists renders a black and white image of the navigable terrain. 
![Color Threshold](color%20threshold.png)

### Additional Color Thresholding
Two additional Color Thresholding functions were written to find rocks and obstacles. The Find rocks function relies on the same process as before but with different filter settings. The settings were configured to find only the yellow rocks. This was accomplished using the interactive version of matplotlib and hovering over the ground rocs extracting the rgb information. The other color thresholding function used was constructed using functions from Open CV library. The image was converted to HSV and the colors of interest were also converted to HSV.  Applying the cv2.inRange and cv2.bitwise_and functions the brown color of the obstacles was extracted but the masked image contained a lot of noise and black areas due to the non-homogenous properties of the terrain. I decided to not incorporate this function into the rover controller because I was able to make the navigation work good enough using only navigable terrain. The images below represent the output from the jupyter notebook for the find rocks function and the cv2 color threshold.

![Find Rocks function](find%20rocks.png)


![CV2 Color Threshold](cv2%20color%20threshold.png)

### Coordinate Transformations
Using the output from the Perspectives Transform to obtain a top down view of the terrain and the Color Thresholding function to return a black and white picture the coordinate transformations can take place transforming the picture into world coordinates. 5 different functions were used to transform the screenshots into world coordinates. In order they follow as: rover_coords, to_polar_coords, rotate_pix, translate_pix, pix_to_world. The purpose of rover_coords extracts the pixel coordinates from the screen shots. To_polar-coords applies SRSS process to the pixel coordinates and extracts the polar coordinates. A translation and rotation are needed to apply the pixel coordinates to rover_coords. The pix_to_world then applies the translation and rotation to the pixel coordinates. A mean average is applied to the information and this is later used as the input to guide the rover through the environment. 
![Coordinate Transform](coordinate%20transform.png)

### Process Image
A function was created that combined all the previous functions into a single function that could take a picture as an input and apply a transform, threshold, and coordinate transformation all at once.  This function was called process image.

### Movie py
A module called movie.py was used to string together a set of images imported from a .csv file. The images had been processed by the Process_Image function and are played out to test the code before trying to connect to the unity environment.

![Coordinate Transform](rover%20movie.mp4)

# Autonmous Navigation and Mapping
I relied on help from the Project Walkthrough video to structure my code and to understand the details of the application. I used the supplied files Perception.py, Drive_rover.py, supporting functions and Desicion.py while adding another one, maneuver.py. To clearly define how changes were made I will walk through each of the files and describe the sections that were added or modified.

### Perception
A majority of the code was from the Rover-Notebook. This file was responsible for transforming the stream of images to information that could detect navigable terrain and rocks. The RGB values were set to 162 for the Red, Green and Blue channels. An additional function was added to make the Rover act more autonomously. This function was rover stuck, and its purpose was to determine if the rover was stuck and to start a counter if this was the case. When the counter was above a user set value, a reverse flag was set to True and the rover would reverse until a speed on -1 m/s was reached controlled from the drive rover file, at which point the Flag would be cleared and the Rover were continue going forward. The value to which to count was found by trial and error. I also tried implementing a time function to do this for me but ultimately it was more strain on the cpu than just using a simple +1 incrementor. The find rocks function was also added to the perception file. this file was a RGB filter set to 90,90,40 respectively. This color Threshold did an excellent job of finding rocks. An additional snippet of code was added on line 88. The purpose of the code was to enable the rover to perform a 180 if it sensed it was at a dead end. On line 187 a `rock_map.any` statement 

### Decision
This file was only modified slightly. I added a bias of +-5 to line 28 using a new class variable called steering offset. This kept the rover near the left side of the wall. I did this to try and help the rover from overlapping areas that it had previously covered and try to raise the fidelity of the simulation.

### Supporting Functions
I don't believe that I made any changes to this file. Its purpose was to convert data for the unity environment, construct output images and manage communications.

### Maneuver
This file was added to support the maneuvering operations of the Rover after a rock sample has been found. The Program consists of simple decision trees that allow the rover to apply throttle, brake and steering control in different steps as the rover approaches the rock sample.  I wanted the rover to approach the samples at orthogonal angles to prevent the rover from getting stuck on rough terrain existing near the side wall. It does a pretty good job at doing this. One this that was done to help was to lower the graphics setting and speed of the rover when approaching, because the rover searches for the stored coordinates of the rock sample. 

### Drive Rover
The Drive Rover file is the main file ran when simulating the Rover in the unity environment. The other files discussed has been imported into drive rover to use.  Additional decision trees were added to the drive rover file.  The first one executes the perception step and the rock maneuver step if samples located are greater than samples collected.  The rover will remain in this rock searching mode until the sample has been picked up.  The normal operation occurs the number of samples found is equal to the number of samples collected.  When this condition exists the perception step and the decision step functions are called.  The other decision points include a reverse flag and a turn 180 flag that execute steering and throttle control to help the rover become unstuck if difficult terrain is found.    

# Conclusion
I was very messy with my code but as I continue to learn I feel like it is easier to organize and be neat.  I ended up with alot of class variables at the end that were not in use.  I decided not to delete these because I wanted to submit the project due to time constraints without cleaning up the code.  The Rover did a fair job at navigating the environment and picking up samples.  The Reverse flag was set to reverse after each sample pickup but this was because the timer I had implemented would acitvate while picking up the sample.  This actually helped my rover to stay on course to reduce the amount of time that the Rover would overlap terrain it had already mapped.  This was because the reverse period allowed the rover to turn and miss the wall before continuing on its way.  I had problems with the simulator when running the program would intermittenly freeze and then when it would unfreeze the communication between the client and server was lost.  This made me have to retry many times.  I did notice that this happend less when my laptop intel core I7 was only running The Udacity rover client and server programs.   




