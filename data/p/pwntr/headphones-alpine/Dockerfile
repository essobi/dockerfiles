FROM alpine:latest  
MAINTAINER Peter Winter <peter@pwntr.com>  
LABEL Description="Simple and lightweight headphones docker container, based
on Alpine Linux." Version="0.1"  
  
# copy init files  
RUN mkdir /setup  
COPY setup/* /setup/  
  
# make the escripts executable and run the setup  
RUN chmod -v +x /setup/*.sh && sh /setup/setup.sh  
  
# delete all the setup files  
RUN rm -r /setup/  
  
# volume mappings  
VOLUME /config /data /downloads /music  
  
# exposes headphone's default port  
EXPOSE 8181  
# not root anymore going forward  
USER headphones  
  
# set some defaults and start nzbget in server and log mode  
ENTRYPOINT ["python", "/headphones/Headphones.py", "--datadir", "/data", "--
config", "/config/headphones.ini"]  

