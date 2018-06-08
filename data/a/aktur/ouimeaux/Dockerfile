FROM python:2.7  
MAINTAINER Michal Rutka (aktur @ github/hub.docker)  
  
# This work only during building the image. Ouimeaux does not use this
variable but  
# reads the config.yml instead.  
ENV OUIMEAUX_SERVER_PORT 15000  
# Install ouimeaux with server  
RUN pip install ouimeaux[server]  
# Bug with "UnicodeError: ('The value must be a native string', 'Access-
Control-Max-Age', 3600)"  
RUN pip install -U gevent==1.1b4  
# Bug with "TypeError: connect() got an unexpected keyword argument 'unique'"  
RUN sed --in-place '134d' /usr/local/lib/python2.7/site-
packages/ouimeaux/server/__init__.py  
# Change default server listening port as it is occupied on Synology (TODO:
make configurable)  
RUN /usr/local/bin/wemo status  
RUN echo "listen: 0.0.0.0:$OUIMEAUX_SERVER_PORT" >> /root/.wemo/config.yml  
  
# expose server's listening port  
EXPOSE $OUIMEAUX_SERVER_PORT  
  
# run server mode  
CMD wemo server  

