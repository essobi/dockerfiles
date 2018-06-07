#--------- Generic stuff all our Dockerfiles should start with so we get
caching ------------  
FROM debian:jessie  
  
RUN apt-get -y update; apt-get -y --force-yes install apt-transport-https  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key 3FF5FFCAD71472C4  
  
RUN echo "deb http://qgis.org/debian-ltr jessie main" >> /etc/apt/sources.list  
RUN echo "deb-src http://qgis.org/debian-ltr jessie main" >>
/etc/apt/sources.list  
  
RUN apt-get -y update; apt-get -y --force-yes install qgis python-qgis  
RUN apt-get -y update; apt-get -y --force-yes install build-essential autoconf
libtool pkg-config  
  
RUN export DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
  
RUN apt-get -y update; apt-get -y --force-yes install pwgen git inotify-tools  
  
#-------------Application Specific Stuff
----------------------------------------------------  
# Install git, xvfb  
RUN apt-get -y update; apt-get -y --force-yes install git xvfb python-
setuptools python-dev libssl-dev libffi-dev python-scipy  
RUN easy_install pip==9.0.1  
ADD REQUIREMENTS.txt /REQUIREMENTS.txt  
ADD REQUIREMENTS-headless.txt /REQUIREMENTS-headless.txt  
ADD REQUIREMENTS-realtime.txt /REQUIREMENTS-realtime.txt  
RUN pip install -r /REQUIREMENTS.txt  
RUN pip install -r /REQUIREMENTS-headless.txt  
RUN pip install -r /REQUIREMENTS-realtime.txt  
# Copy ubuntu fonts  
RUN apt-get -y update; apt-get -y --force-yes install wget unzip  
ADD ubuntu-font-family-0.83.zip /ubuntu-font-family-0.83.zip  
RUN unzip ubuntu-font-family-0.83.zip  
RUN mv ubuntu-font-family-0.83 /usr/share/fonts/truetype/ubuntu-font-family  
RUN fc-cache -f -v  
  
# Clone source code  
RUN mkdir -p /home/realtime/src  
WORKDIR /home/realtime/src  
ARG INASAFE_REALTIME_TAG=realtime-backport-cherry-pick  
RUN git clone \--branch ${INASAFE_REALTIME_TAG} \--depth 1
https://github.com/inasafe/inasafe-realtime.git inasafe  
  
# Called on first run of docker - will run make-latest-shakemap.sh  
ADD entry-point.sh /entry-point.sh  
# Add bash service to monitor shakemaps folder  
ADD shakemaps_monitor.sh /shakemaps_monitor.sh  
RUN chmod 0755 /entry-point.sh  
  
CMD /entry-point.sh  

