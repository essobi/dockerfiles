FROM wow73611/ubuntu  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
apt-get update -y && \  
apt-get install -y python2.7 python2.7-dev python-pip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
RUN pip install virtualenv  
  
CMD ["bash"]  

