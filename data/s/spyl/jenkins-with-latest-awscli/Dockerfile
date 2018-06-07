FROM jenkins  
  
MAINTAINER Oleksii Semilietov <spylik@gmail.com>  
LABEL "description"="Image contain latest awscli on top on official Jenkins
image."  
USER root  
RUN curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli  
USER jenkins  

