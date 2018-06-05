# To run pytest successfully in any docker container, the container must be
baseed on ubuntu 14.04;  
# or, more correctly, it cannot be based on ubuntu 16.04, which is what an
untagged `FROM ubuntu` loads.  
# No online documentation of why this is so has been found.  
FROM ubuntu:14.04  
MAINTAINER Rod Glover <rglover@uvic.ca>  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && \  
apt-get -yq install \  
libpq-dev \  
python3 \  
python3-dev \  
python3-pip \  
postgresql-client  
  
ADD . /app  
WORKDIR /app  
  
RUN pip3 install -U pip  
RUN pip3 install -i https://pypi.pacificclimate.org/simple/ -r
requirements.txt  
RUN pip3 install .  
  
EXPOSE 8000  
CMD devserver.py -p 8000 -t  

