FROM debian  
MAINTAINER Ryan Grieve <me@ryangrieve.com>  
  
# no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# update apt cache, upgrade the system and install the system utils we need  
RUN apt-get update --fix-missing && apt-get upgrade -y  
RUN apt-get install -y python python-pip  
  
# install sphinx  
RUN pip install radon  
  
CMD radon cc /app  

