FROM timn/fawkes-robotino:2016-f25-kinetic-simbase  
MAINTAINER Tim Niemueller <niemueller@kbsg.rwth-aachen.de>  
  
# ROS_DISTRO set by fedora-ros layer  
# Get and compile Fawkes  
# Use generic optimization so that the resulting image works on more
platforms.  
# Enable the old 2015 agent, only that has the full model of the production.  
RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \  
cd /opt && \  
curl -O https://files.fawkesrobotics.org/releases/fawkes-
robotino-2016-2.tar.bz2 && \  
tar xf fawkes-robotino-2016-2.tar.bz2 && \  
cd fawkes-robotino && \  
sed -i -e 's/CFLAGS_EXTRA += -g/CFLAGS_EXTRA += -m64 -mtune=generic -g/g'
etc/buildsys/config.mk && \  
sed -e 's/\\(agent: rcll2016\/rcll2016\\)/# \1/;s/# \\(agent:
llsf2015\/llsf2015\\)/\1/' cfg/conf.d/clips-agent.yaml && \  
make all gui"  
  
# Get and compile ROS RCLL sim bits  
RUN /bin/bash -c "source /etc/profile && \  
mkdir -p /opt/ros/catkin_ws_${ROS_DISTRO}_rcll_sim/src; \  
cd /opt/ros/catkin_ws_${ROS_DISTRO}_rcll_sim; \  
wstool init -j $(nproc) src ../rcll-sim.rosinstall; \  
rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -y; \  
catkin_make_isolated --install --install-space /opt/ros/$ROS_DISTRO \  
-DCMAKE_BUILD_TYPE=$ROS_BUILD_TYPE || exit $?; \  
rm -rf *_isolated; \  
"  
  
COPY ./rcll-run-sim.sh /bin/  
ENTRYPOINT ["/bin/rcll-run-sim.sh"]  
  

