FROM centos:latest  
MAINTAINER github.com/blindly  
  
# Install wget  
RUN yum install wget -y  
  
# Install Python SetupTools  
RUN yum install python-setuptools -y  
  
# Download Hatta Wiki  
RUN mkdir /hatta  
WORKDIR /hatta  
RUN wget https://bitbucket.org/thesheep/hatta/downloads/hatta-1.6.4.zip.py -O
/hatta/hatta-1.6.4.zip.py  
  
EXPOSE 8080  
CMD ["python", "/hatta/hatta-1.6.4.zip.py"]  

