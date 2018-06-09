  
FROM ros:kinetic  
  
# HACK: http://stackoverflow.com/questions/25193161/chfn-pam-system-error-
intermittently-in-docker-hub-builds  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
COPY public.key /tmp/  
  
RUN apt-get update  
RUN apt-get install -y curl software-properties-common python-software-
properties  
RUN apt-key add /tmp/public.key  
RUN apt-add-repository http://lcas.lincoln.ac.uk/ubuntu/main  
RUN apt-get update && apt-get install -y \  
ros-kinetic-strands-* ros-kinetic-rospack python-rosinstall-generator python-
wstool  
RUN bash -c "rm -rf /etc/ros/rosdep; source /opt/ros/kinetic/setup.bash;\  
rosdep init"  
RUN curl -o /etc/ros/rosdep/sources.list.d/20-default.list
https://raw.githubusercontent.com/LCAS/rosdistro/master/rosdep/sources.list.d/20-default.list  
RUN curl -o /etc/ros/rosdep/sources.list.d/50-lcas.list
https://raw.githubusercontent.com/LCAS/rosdistro/master/rosdep/sources.list.d/50-lcas.list  
RUN mkdir -p /root/.config/rosdistro/  
RUN echo "index_url: https://raw.github.com/lcas/rosdistro/master/index.yaml"
> /root/.config/rosdistro/index.yaml  
RUN bash -c "source /opt/ros/kinetic/setup.bash;\  
export
ROSDISTRO_INDEX_URL="https://raw.github.com/lcas/rosdistro/master/index.yaml";
\  
rosdep update"  
RUN mkdir -p workspace/src  
WORKDIR workspace/src  
RUN bash -c 'source /opt/ros/kinetic/setup.bash;\  
export
ROSDISTRO_INDEX_URL="https://raw.github.com/lcas/rosdistro/master/index.yaml";
\  
catkin_init_workspace . ; \  
/opt/ros/kinetic/bin/rospack list | grep ^strands | cut -f1 -d" " > strands-
package.lst; \  
/opt/ros/kinetic/bin/rospack list | grep ^scitos | cut -f1 -d" " >> strands-
package.lst; \  
cat strands-package.lst; \  
rosinstall_generator --upstream-development `cat strands-package.lst` >
strands.rosinstall; \  
cat strands.rosinstall; \  
wstool init; \  
wstool merge strands.rosinstall; \  
wstool update; \  
rosdep install -y --as-root=apt:false -i --from-paths . \  
'  
RUN apt-get install -y python-bloom vim nano less  

