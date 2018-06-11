# Pull base image.  
FROM debian:wheezy  
  
# sources.list  
# ADD sources.list.wheezy /etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y unzip wget vim  
RUN apt-get install -y supervisor  
VOLUME ["/etc/supervisor/conf.d"]  
  
CMD ["bash"]

