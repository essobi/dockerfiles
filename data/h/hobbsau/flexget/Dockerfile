FROM alpine:edge  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE "py2-pip tzdata"  
# Install packages using --no-cache to update index and remove unwanted files
and use pip to install the rest  
RUN apk add --no-cache $PACKAGE && \  
pip install --upgrade pip && \  
pip install --upgrade setuptools && \  
pip install pytest pytest-runner && \  
pip install flexget && \  
cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime && \  
echo "Australia/Sydney" > /etc/timezone && \  
# Add a user to run as non root  
adduser -D -g '' flexget  
  
USER flexget  
ENV HOME /home/flexget  
  
CMD ["/usr/bin/flexget","daemon","start"]  
  

