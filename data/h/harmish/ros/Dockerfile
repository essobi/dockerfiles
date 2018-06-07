FROM harmish/ros:jade-navigation  
# install gdbserver  
RUN apt-get update && \  
apt-get install -y \  
gdbserver && \  
#  
# replace catkin (with Catch) and catkin_pkg  
git clone https://github.com/harmishhk/catkin -b jade-catch
/catkin_ws/src/catkin && \  
/bin/bash -c "source /opt/ros/jade/setup.bash && catkin_make
-DCMAKE_INSTALL_PREFIX=/opt/ros/jade -C /catkin_ws install" && \  
git clone https://github.com/harmishhk/Catch /catch && \  
/bin/bash -c "python /catch/scripts/generateSingleHeader.py && mkdir -p
/opt/local/catch/include && cp /catch/single_include/catch.hpp
/opt/local/catch/include/catch.hpp" && \  
git clone https://github.com/harmishhk/catkin_pkg /catkin_pkg && \  
/bin/bash -c "cd /catkin_pkg && python setup.py install" && \  
rm -rf /catkin_ws /catch /catkin_pkg && \  
#  
# clean-up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CMAKE_INCLUDE_PATH /opt/local/catch/include:$CMAKE_INCLUDE_PATH  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["bash", "/entrypoint.sh"]  
CMD ["bash"]  

