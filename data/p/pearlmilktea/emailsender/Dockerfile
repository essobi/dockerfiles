############################################################  
# Dockerfile to send email from python  
# Based on "Ubuntu trusty"  
############################################################  
  
From ubuntu:trusty  
MAINTAINER pearkmilktea  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y \  
python \  
postfix  
  
#COPY main.cf /etc/postfix  
  
RUN mkdir /home/files  
WORKDIR /home/files  
  
ENTRYPOINT ["/bin/sh", "-c", "service postfix start ; /bin/sh"]  

