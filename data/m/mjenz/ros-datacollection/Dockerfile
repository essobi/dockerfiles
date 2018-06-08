FROM mjenz/ros-indigo-perception  
  
# Build bag_tools from source and install in an overlay  
WORKDIR /tmp/catkin_ws  
RUN mkdir src && \  
git clone https://github.com/srv/srv_tools.git src/srv_tools && \  
cd src/srv_tools && git reset --hard efa11bb && cd ../.. && \  
. /opt/ros/indigo/setup.sh && \  
catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/indigo_local install && \  
rm -rf /tmp/catkin_ws  
  
COPY ./ros_datacollection_entrypoint.sh /  
ENTRYPOINT ["/ros_datacollection_entrypoint.sh"]  
CMD ["bash"]  

