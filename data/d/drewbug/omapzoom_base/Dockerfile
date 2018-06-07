# BUILD-USING: docker build -t drewbug/omapzoom_base .  
FROM ubuntu:12.04  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
MAINTAINER Drew Carey Buglione <me@drewb.ug>  
  
RUN mkdir omapzoom  
WORKDIR omapzoom  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget ca-certificates
python git  
RUN wget -O /usr/local/bin/repo http://commondatastorage.googleapis.com/git-
repo-downloads/repo && chmod +x /usr/local/bin/repo  
  
RUN repo init -u git://git.omapzoom.org/platform/omapmanifest.git -b 25.x  
RUN repo sync frameworks/base  
RUN repo sync vendor/ti/zoom2  

