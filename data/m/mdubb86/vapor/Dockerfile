FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \  
openjdk-8-jdk \  
unzip \  
mediainfo \  
git \  
maven  
  
EXPOSE 8080  
# Install h2  
COPY h2-2016-10-31.zip /opt/  
RUN cd /opt && unzip /opt/h2-2016-10-31.zip  
  
# Set the entry point  
ENTRYPOINT ["/init"]  
  
# Install services  
COPY services /etc/services.d  
  
# Install init.sh as init script  
COPY init.sh /etc/cont-init.d/  
  
# Download and extract s6 init  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  

