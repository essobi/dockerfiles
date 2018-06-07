#######################  
#  
# docker run -ti --rm \  
# -e DISPLAY=$DISPLAY \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# kanalfred/ui  
#  
# Give docker user permission for local x11  
# xhost +local:docker  
#  
# firefox:  
# docker run -it --rm -v /usr/share/themes:/usr/share/themes -v $HOME:/$HOME
-v `pwd`:/app -w /app -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
kanalfred/ui firefox  
# Sublime:  
# docker run -it --rm -v /usr/share/themes:/usr/share/themes -v $HOME:/$HOME
-v `pwd`:/app -w /app -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
kanalfred/ui sublime -new  
#  
# refer  
# http://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-
docker-container/25280523#25280523  
# http://stackoverflow.com/questions/25281992/alternatives-to-
ssh-x11-forwarding-for-docker-containers/25334301#25334301  
# https://unix.stackexchange.com/questions/196677/what-is-tmp-x11-unix  
#######################  
FROM ubuntu:16.04  
  
#RUN apt-get update && apt-get install -y firefox  
RUN \  
apt-get update && apt-get install -y firefox=45* && \  
apt-get install -y rdesktop && \  
apt-get install -y libcanberra-gtk* && \  
#apt-get update &&  
# install add-apt-repository  
apt-get install -y software-properties-common && \  
# x11 themes support  
apt-get install -y gnome-themes-standard && \  
apt-get install -y gtk2-engines && \  
apt-get install -y gtk2-engines-murrine && \  
apt-get install -y dbus-x11  
#RUN apt-get install -y vim  
  
# Sublime 3  
RUN \  
add-apt-repository ppa:webupd8team/sublime-text-3 && \  
apt-get update && \  
apt-get install -y sublime-text-installer && \  
ln -s /opt/sublime_text/sublime_text /usr/bin/sublime  
#RUN apt-get install -y dbus libdbus-1-dev libxml2-dev dbus-x11  
  
# Replace 1000 with your user / group id  
#RUN export uid=1000 gid=1000 && \  
# mkdir -p /home/developer && \  
# echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
# echo "developer:x:${uid}:" >> /etc/group && \  
# echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
# chmod 0440 /etc/sudoers.d/developer && \  
# chown ${uid}:${gid} -R /home/developer  
#  
#USER developer  
#ENV HOME /home/developer  
#CMD /usr/bin/firefox  
#CMD /opt/sublime_text/sublime_text  
#ENTRYPOINT ["/bin/bash","-c"]  
#CMD /opt/sublime_text/sublime_text  
#CMD ["sublime"]  

