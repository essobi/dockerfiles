FROM python:2.7  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
RUN apt-get update && \  
apt-get install -y git &&\  
git clone https://github.com/munki/munki.git /munki-tools  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
VOLUME /munki_repo  
CMD /run.sh  

