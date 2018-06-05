FROM mjenz/ros-indigo-perception  
  
RUN apt-get update && \  
apt-get install -y ros-indigo-pointgrey-camera-driver && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./bumblebee2.launch /  
CMD ["roslaunch", "/bumblebee2.launch"]  
  

