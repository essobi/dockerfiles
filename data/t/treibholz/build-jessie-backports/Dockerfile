FROM buildpack-deps:jessie  
MAINTAINER Klaus Umbach <klaus+docker@uxix.de>  
  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y ssmtp python-support debhelper devscripts git ca-
certificates vim sudo ncurses-term && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
useradd -m -u 12345 --skel /etc/skel builder  
  
COPY sudoers /etc/sudoers  
  
WORKDIR /home/builder  
USER builder  

