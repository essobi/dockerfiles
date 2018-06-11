FROM hedlund/ubuntu:xenial  
MAINTAINER Henrik Hedlund <henrik@hedlund.im>  
  
ENV JSPP_VERSION 0.4.1  
# Download and install JS++  
RUN curl -o /tmp/JS++.tar.gz
https://onux.r.worldssl.net/jspp/downloads/JS++-${JSPP_VERSION}-linux_x64.tar.gz
&& \  
tar zvxf /tmp/JS++.tar.gz -C /opt && \  
chown -R root:root /opt/JS++ && \  
ln -s /opt/JS++/js++ /usr/local/bin/js++ && \  
rm /tmp/JS++.tar.gz && \  
mkdir -p /code  
  
# Setup the workdir  
VOLUME [ "/code" ]  
WORKDIR /code  
  
# The js++ command will be the star of the image  
ENTRYPOINT [ "js++" ]  

