# Image-Coordinate-Tool
A python CL tool to show central origin based 2D coordinates of a fullhd image(1920x1080) loaded in a smaller window. The tool displays coordinates wrt the image original size (1920x1080), and not the window size. 

## Usage
- coordinates.exe -i "sample.jpg" ----  to launch the app with default settings and sample.jpg image. Default window dimensions are 960x540.
- coordinates.exe -i "sample.jpg" -g ---- adds a central grid
- coordinates.exe -i "sample.jpg" -w 1280 -l 720 ----- changes window dimensions to 1280x720
- coordinates.exe -i "sample.jpg" -w 1600 -l 900 ----- changes window dimensions to 1600x900
- coordinates.exe -i "sample.jpg" -w 1920 -l 1080 ----- changes window dimensions to 1920x1080
