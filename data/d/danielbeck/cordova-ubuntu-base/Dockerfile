# VERSION: 0.0.3  
FROM ubuntu:14.04  
MAINTAINER Daniel Beck "d.danielbeck@googlemail.com"  
RUN apt-get install -y vim click click-dev schroot software-properties-common  
RUN add-apt-repository ppa:cordova-ubuntu/ppa  
RUN add-apt-repository ppa:ubuntu-sdk-team/ppa  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install cordova-cli -y  
#RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get autoremove -y  
RUN apt-get clean  
  
  
# Download libraries  
RUN cd /tmp && cordova create fakeapp && cd /tmp/fakeapp && cordova platform
add ubuntu  
  
# This does not work, because "build" cannot be runned in the privileged mode.  
#RUN cd /root && click chroot -aarmhf -f ubuntu-sdk-14.10 create  
#RUN click chroot -aarmhf -f ubuntu-sdk-14.10 install libicu-dev:armhf
qtfeedback5-dev:armhf qtpim5-dev:armhf qtsystems5-dev:armhf  
# Check the config.xml file. The icon file might be missing  
#RUN cd /tmp/fakeapp && cordova build --device  
# Delete fake application, since it isn't needed anymore  
#RUN cd ~/ && rm -rf /tmp/fakeapp  
  
VOLUME ["/data"]  
VOLUME ["/tmp"]  
WORKDIR /tmp  
#ENTRYPOINT ["/usr/local/bin/cordova"]  
#CMD ["-h"]  
#ENTRYPOINT ["/bin/bash"]  

