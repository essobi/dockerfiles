#Use an official Python runtime as a parent image  
FROM ubuntu:18.04  
RUN apt update  
RUN apt install sudo  
  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
  
RUN sudo apt install -y libgl1-mesa-dev libpulse-mainloop-glib0
gstreamer1.0-libav gstreamer1.0-x libfontconfig1-dev libfreetype6-dev
libx11-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev
libx11-xcb-dev libxcb-glx0-dev  
  
USER docker  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
ADD . /app  
  
# Run app.py when the container launches  
CMD ["./AppRun", ""]  

