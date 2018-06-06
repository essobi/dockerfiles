FROM ubuntu:latest  
  
WORKDIR /emscripten  
RUN apt-get update && \  
apt-get install -y python2.7 xz-utils default-jre wget && \  
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1 && \  
wget https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-
portable.tar.gz && \  
tar --strip-components=1 -xzvf emsdk-portable.tar.gz && \  
rm emsdk-portable.tar.gz && \  
rm -rf /var/lib/apt/lists/*  
  
COPY emsdk.sh /etc/profile.d/emsdk.sh  
WORKDIR /  
CMD ["/bin/bash", "-l"]  

