FROM phusion/baseimage  
MAINTAINER http://www.viur.is  
  
RUN apt-get update && \  
apt-get install -y apt-utils && \  
apt-get install -y --fix-missing \  
curl \  
git \  
perl \  
unzip \  
nodejs \  
npm \  
python-jinja2 \  
python-pil \  
python-pip \  
python-yaml \  
python-requests \  
python \  
python-dev && \  
ln -fs /usr/bin/nodejs /usr/local/bin/node && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]  

