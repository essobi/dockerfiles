FROM python:3  
MAINTAINER Yuya Kusakabe <yuya.kusakabe@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y git mercurial texlive-full xzdec && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip install sphinx  

