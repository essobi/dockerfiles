FROM python:2  
LABEL version="0.1.0" description="insight"  
MAINTAINER Victor Clark <resume@victorclark.org>  
  
#Update image:  
RUN apt-get update  
  
#replace sh with bash:  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
#Clone field_recommend  
WORKDIR /  
RUN git clone https://github.com/0victor0/insight.git  
  
#Put out the welcome mat  
WORKDIR /insight  
ENTRYPOINT python

