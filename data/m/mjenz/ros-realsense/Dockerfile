FROM mjenz/ros-indigo-perception  
  
RUN apt-get update && \  
apt-get install -y ros-indigo-realsense-camera && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["roslaunch", "realsense_camera", "r200_nodelet_rgbd.launch"]  
  

