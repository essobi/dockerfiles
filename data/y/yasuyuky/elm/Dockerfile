FROM ubuntu:latest  
MAINTAINER yasuyuky <yasuyuki.ymd@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get -y install git npm nodejs-legacy  
RUN npm install -g elm  
RUN cd / && mkdir source  
WORKDIR source  
CMD ["bash"]  
ENV LANG=C.UTF-8  
ENV LC_ALL=C.UTF-8  

