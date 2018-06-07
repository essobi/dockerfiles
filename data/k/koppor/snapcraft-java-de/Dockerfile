FROM ubuntu:rolling  
  
# use nearby German mirror  
RUN sed -i "s/archive/de5.archive/" /etc/apt/sources.list  
  
RUN apt-get update -qq &&\  
apt-get dist-upgrade -qq &&\  
apt-get install -y default-jre-headless default-jdk-headless openjfx ca-
certificates-java locales lxd snapcraft &&\  
apt-get clean -qq&&\  
apt-get autoremove --purge -qq  
  
# snapcraft requires properly configured locales  
RUN locale-gen && update-locale LC_ALL=C.UTF-8 LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  

