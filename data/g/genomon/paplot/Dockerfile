FROM python:2.7.14  
MAINTAINER aokad <aokad@hgc.jp>  
  
RUN apt-get -y update && \  
apt-get install -y wget unzip && \  
\  
wget https://github.com/Genomon-Project/paplot/archive/v0.5.5.zip && \  
unzip v0.5.5.zip && \  
rm v0.5.5.zip && \  
cd paplot-0.5.5; python setup.py build install  
  
CMD ["/bin/bash"]  

