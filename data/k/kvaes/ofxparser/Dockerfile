#  
# OfxParser Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-ofxparser/  
# Author : Karim Vaes  
#  
# Use Phusion Baseimage as a start  
FROM phusion/baseimage  
  
# Install php5-cli & cleanup  
RUN apt-get update && apt-get -y install php7.0-cli && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Let's prep the OfxParser install  
RUN mkdir -p /ofx/bin && mkdir -p /ofx/in && mkdir -p /ofx/out  
  
# Pull the latest ofxparser source  
ENV HOME /root  
COPY config.php /ofx/bin/  
COPY csv2oxf.php /ofx/bin/  
COPY parser.php /ofx/bin/  
  
# Setup Volumes  
VOLUME ["/ofx/in"]  
VOLUME ["/ofx/out"]  
  
# Define default command.  
CMD ["/usr/bin/php7.0", "/ofx/bin/csv2oxf.php"]  

