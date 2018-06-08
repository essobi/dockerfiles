FROM ubuntu:16.10  
# install first  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install wget make gcc python2.7 python-pip git && apt-get -y clean;
\  
pip install --upgrade pip  
  
  
# install rime  
RUN pip install git+https://github.com/icpc-jag/rime; \  
pip install -U git+https://github.com/icpc-jag/rime;  

