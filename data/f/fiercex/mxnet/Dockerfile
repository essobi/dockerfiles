FROM ubuntu:16.04  
MAINTAINER fiercex <fiercewind@outlook.com>  
#RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
python wget gcc python-opencv  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
RUN pip install mxnet graphviz captcha  
  
RUN rm -rf get-pip.py  

