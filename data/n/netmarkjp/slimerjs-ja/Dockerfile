FROM centos:centos7  
RUN yum -y install git xulrunner xorg-x11-server-Xvfb vlgothic-fonts  
RUN cd /opt && git clone https://github.com/laurentj/slimerjs.git  
RUN cd /opt/slimerjs && git checkout RELEASE_0.9.5  
VOLUME ["/data"]  
ENTRYPOINT ["xvfb-run", "/opt/slimerjs/src/slimerjs"]  

