  
FROM ros:kinetic-ros-core-xenial  
  
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
ros-kinetic-rospack ros-kinetic-catkin python-rosinstall-generator python-
wstool \  
python-bloom vim nano less ssh python-pip  
  
RUN pip install bloom  
  
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
  
ENV ROSDISTRO_INDEX_URL
https://raw.github.com/lcas/rosdistro/master/index.yaml  
  
RUN mkdir -p workspace/src  
WORKDIR workspace/src  
RUN bash -c 'source /opt/ros/kinetic/setup.bash;\  
export
ROSDISTRO_INDEX_URL="https://raw.github.com/lcas/rosdistro/master/index.yaml";
\  
catkin_init_workspace . ; \  
wstool init; \  
'  
  
ADD git-catkin-build.sh /usr/local/bin  
  

