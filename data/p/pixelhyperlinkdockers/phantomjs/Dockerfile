# PixelHyperlink PhantomJS Docker  
#  
# VERSION 1.1.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with apache and 64bit
PhantomJS service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.1.0"  
LABEL com.pixelhyperlink.docker.phantomjs.version="1.1.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.phantomjs.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.phantomjs.version.is-production="true"  
  
# Install apache, PHP, and supplimentary programs.  
RUN apt-get update && \  
apt-get install -y libfontconfig  
  
# Expose phantomjs.  
EXPOSE 8910  
# Copy phantomjs  
COPY ./phantomjs /opt/phantomjs  
RUN chmod 755 /opt/phantomjs  
  
# Create phantomjs user  
RUN useradd --system --uid 72379 -m --shell /usr/sbin/nologin phantomjs  
  
# Copy server start up scripts  
COPY ./phantomjs_entrypoint.sh /opt/phantomjs_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/phantomjs_entrypoint.sh  
  
USER phantomjs  
  
ENTRYPOINT ["/opt/phantomjs_entrypoint.sh"]  

