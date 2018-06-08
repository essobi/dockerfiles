#Use debian base image, it comes with python  
FROM debian:jessie  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the current directory contents into the container at /app  
COPY . /app  
  
# Install PyGObject bindings  
RUN apt-get update && apt-get install -y \  
gir1.2-gst-plugins-base-1.0 \  
gstreamer1.0-plugins-good \  
gstreamer1.0-alsa \  
gstreamer1.0-libav \  
python3-gi \  
python3-pip  
  
RUN usermod -a -G audio root  
  
# Install any needed packages specified in requirements.txt  
RUN pip3 install -r requirements.txt  
  
# Run app.py when the container launches  
CMD ["echo", "command_server.py"]  

