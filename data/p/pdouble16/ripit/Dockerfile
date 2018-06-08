FROM blitznote/debootstrap-amd64:16.04  
MAINTAINER Patrick Double <pat@patdouble.com>  
  
RUN rm -rf /var/lib/apt/lists/* &&\  
apt-get -q update &&\  
apt-get install -qy --allow-downgrades ripit lame eyed3 imagemagick ffmpeg &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
CMD ["/bin/bash"]  
  

