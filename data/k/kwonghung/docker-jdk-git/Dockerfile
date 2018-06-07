FROM kwonghung/docker-jdk:8-oracle  
LABEL maintainer="kwonghung.yip@gmail.com"  
  
SHELL ["/bin/bash","-c"]  
  
RUN apt-get update; \  
apt-get install -y git; \  
apt-get clean;  
  
WORKDIR /root/build  
  
CMD ["bash"]

