FROM mjenz/ros-indigo-gui  
  
# Install packages for Turtlebot, my packages, and just ones I use  
RUN sudo apt-get update && \  
sudo apt-get install -y \  
ros-indigo-turtlebot-simulator \  
ros-indigo-turtlebot-teleop \  
ros-indigo-turtlebot-rviz-launchers \  
tmux \  
ipython \  
python-pip && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo pip install cython nose  
  
# Cache gazebo models for turtlebot_world.world and map_creator.world  
# Loosely based on
https://github.com/PX4/containers/blob/master/docker/px4-dev/scripts/cache-
gazebo-models.bash  
RUN mkdir -p "$HOME/.gazebo/models" && \  
mkdir /tmp/models && \  
cd /tmp/models && \  
for m in "cube_20k" "dumpster" "jersey_barrier" "ground_plane" "sun"
"willowgarage"; do \  
curl -Os "http://models.gazebosim.org/$m/model.tar.gz" && \  
tar -zvxf model.tar.gz && \  
cp -vfR $m "$HOME/.gazebo/models/"; \  
rm model.tar.gz; \  
done && \  
cd .. && rm -r /tmp/models  
  
COPY tmux.conf /home/ros/.tmux.conf  

