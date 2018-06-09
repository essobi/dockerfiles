FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Mart QIN  
  
# Update the sources list  
RUN apt-get update  
RUN apt-get install -y git bridge-utils libssl-dev gcc g++ build-essential
make libevent-dev libxml2-dev libxslt-dev tar zlib1g.dev openssl  
  
# Install Python 2.7.8  
RUN apt-get install -y -q python2.7 python2.7-dev  
RUN apt-get install -y -q python-distribute python-pip  
  
# Install scipy and numpy  
# RUN apt-get install python-scipy  
# RUN apt-get install python-numpy  
# prepare env for git  
RUN touch ~/.git-credentials  
RUN echo "https://martqin:beiyuan987521@github.com" > ~/.git-credentials  
RUN git config --global credential.helper store  
# clone TaggingTool code from github  
# Set the default directory where CMD will execute  
WORKDIR /Tagging  
RUN git clone https://martqin@github.com/AcxiomSwateam/TaggingTool_EC2.git  
  
# Create virtualenv and install requirements:  
RUN pip install -r /Tagging/TaggingTool_EC2/requirements.txt  
  
# Expose ports  
EXPOSE 80  
# CMD python TaggingTool.py  

