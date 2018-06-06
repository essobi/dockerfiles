FROM python:3  
MAINTAINER Martin Peters  
  
# create err user and set it's home as working dir  
RUN useradd --home-dir /err err  
RUN mkdir -p /err/data && chown err:err -R /err  
WORKDIR /err  
  
# add config.py  
ADD config.py /err/config.py  
  
# define data as volume  
VOLUME /err/data  
  
# install errbot and dependencies for backends  
RUN pip install errbot~=5.0 sleekxmpp pyasn1 pyasn1-modules irc hypchat
slackclient python-telegram-bot  
  
# define command  
USER err  
CMD ["/usr/local/bin/errbot"]  

