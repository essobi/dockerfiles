FROM jsurf/rpi-raspbian:latest  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && \  
apt-get -y install devscripts equivs build-essential debhelper wget fakeroot
git && \  
rm -rf /var/lib/apt/lists/*  
  
RUN [ "cross-build-end" ]  

