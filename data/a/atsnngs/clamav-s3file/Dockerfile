FROM ubuntu:16.04  
MAINTAINER Atsushi Nagase<a@ngs.io>  
  
RUN apt-get -y update && \  
apt-get -y install clamav python-pip curl && \  
pip install awscli  
  
RUN sed -i -e "s/^NotifyClamd/#NotifyClamd/g" /etc/clamav/freshclam.conf &&
freshclam  
ADD scan-s3file /usr/local/bin/scan-s3file  
  
ENTRYPOINT ["/usr/local/bin/scan-s3file"]  

