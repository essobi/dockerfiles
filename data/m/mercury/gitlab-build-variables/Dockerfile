FROM python:3.6-alpine  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir /home/gitlab-build-variables-manager  
WORKDIR /home/gitlab-build-variables-manager  
ADD . .  
  
RUN ls  
  
RUN python setup.py install  
  
# Set workdir and entrypoint  
WORKDIR /tmp  
ENTRYPOINT []  

