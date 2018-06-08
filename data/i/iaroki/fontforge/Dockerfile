FROM ubuntu:16.04  
MAINTAINER iaroki  
RUN apt-get update && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:fontforge/fontforge -y && \  
apt-get update && \  
apt-get install fontforge -y --no-install-recommends  
RUN useradd -u 1000 -m -G video iaroki  
USER iaroki  
CMD ["fontforge"]  

