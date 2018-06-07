FROM ju55i/plone-base:4.3-latest  
MAINTAINER Jussi Talaskivi <jptalask@gmail.com>  
  
# Everything is run as a zope user  
WORKDIR /buildout  
ADD buildout.cfg /buildout/  
RUN bin/buildout  
CMD sed -i "s/REPLACEME/$HOSTNAME/g" parts/instance/etc/zope.conf ;
bin/instance console  
  
EXPOSE 8080  

