FROM ubuntu:latest as builder  
ARG IMAGE=rancheros-0.3.0-gz.img  
RUN apt-get update && apt-get install -y wget  
RUN cd / && wget https://s3-us-west-1.amazonaws.com/sheng/qcow2/$IMAGE  
  
FROM haximilian/ranchervm-base:latest  
LABEL maintainer="haximilian@gmail.com"  
COPY \--from=builder $IMAGE /base_image/image.img  
CMD ["-m 512m"]  

