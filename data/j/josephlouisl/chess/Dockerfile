FROM python:3.6  
MAINTAINER Dockerfiles  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
cmake \  
apt-utils \  
virtualenv \  
libboost-all-dev &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/chessonline  
WORKDIR /etc/chessonline  
COPY . .  
RUN bash build.sh  
ADD start.sh /etc/chessonline/  
EXPOSE 8000  
CMD ["bash", "start.sh"]

