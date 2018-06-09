FROM ubuntu:14.04  
MAINTAINER Ted Reed "ted.reed@gmail.com"  
RUN apt-get update -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip groff-base  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy curl  
RUN pip install awscli  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  

