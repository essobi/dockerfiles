FROM ubuntu:latest  
MAINTAINER Hoanh An <hoanhan@bennington.edu>  
  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
RUN apt-get update && apt-get install -y \  
python3-dev \  
python3-setuptools \  
python3-pip \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
COPY * ./  
RUN ./install_requirements.sh  
  
EXPOSE 5000  
ENV FLASK_APP=hub.py  
CMD ./start.sh  

