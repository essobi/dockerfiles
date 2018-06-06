FROM node:stretch  
  
# https://github.com/ether/etherpad-lite#user-content-gnulinux-and-other-unix-
like-systems  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
gzip \  
libssl-dev \  
pkg-config \  
python  
  
RUN git -C /opt clone git://github.com/ether/etherpad-lite.git  
  
RUN /opt/etherpad-lite/bin/installDeps.sh  
  
EXPOSE 9001  
CMD ["/opt/etherpad-lite/bin/run.sh", "--root"]  

