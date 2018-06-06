FROM debian:jessie-backports  
MAINTAINER Danny Edel <mail@danny-edel.de>  
  
# Packs the HTML5 validator.nu from  
# https://github.com/validator/validator  
# into a docker container.  
# RUN sed -i -e 's|httpredir.debian.org|ftp.us.debian.org|g'
/etc/apt/sources.list  
RUN apt-get update && \  
apt-get -y install openjdk-8-jre unzip  
  
# FIXME: Keep this URL up to date  
ADD
https://github.com/validator/validator/releases/download/16.6.29/vnu.jar_16.6.29.zip
/opt/  
  
RUN unzip -d /opt/ /opt/vnu.jar_*.zip  
  
COPY validate /usr/bin  
COPY validate-pedantic /usr/bin  
  
# By default, run the validate-pedantic script  
# on the current working directory  
CMD [ "/usr/bin/validate-pedantic", "./" ]  

