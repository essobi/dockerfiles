FROM blacklabelops/swarm-jdk8  
MAINTAINER Kenichiro Ota <oota_ken@hotmail.com>  
  
  
# Need root to build image  
USER root  
  
# install chrome  
# from https://hub.docker.com/r/truhuynh/chrome/~/dockerfile/  
RUN yum clean all && rm -rf /var/cache/yum/*  
#RUN yum -y update; yum clean all  
RUN yum -y install mesa-dri-drivers libexif libcanberra-gtk2 libcanberra; yum
clean all  
  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
/root/google-chrome-stable_current_x86_64.rpm  
  
RUN yum -y install /root/google-chrome-stable_current_x86_64.rpm; yum clean
all  
ADD chromedriver /usr/bin/  
RUN chmod 755 /usr/bin/chromedriver  
  
# install firefox  
# from https://hub.docker.com/r/kevensen/centos-vnc-firefox/~/dockerfile/  
RUN yum install -y firefox spice-xpi; yum clean all; rm -rf /var/cache/yum  
  
# install and setup Xvfb  
# from https://github.com/SeleniumHQ/docker-selenium/tree/master/NodeBase  
RUN yum install -y xorg-x11-server-Xvfb dbus-x11  
RUN dbus-uuidgen > /etc/machine-id  
  
# Switch back to user jenkins  
USER $CONTAINER_UID  

