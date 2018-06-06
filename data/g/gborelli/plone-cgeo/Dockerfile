FROM abstracttechnology/plone:5.0  
MAINTAINER Giorgio Borelli <giorgio@giorgioborelli.it>  
  
USER root  
  
# Update buildout.cfg  
COPY buildout.cfg buildout.cfg  
COPY cgeo.cfg cgeo.cfg  
COPY entrypoint.sh entrypoint.sh  
COPY data data  
RUN chown -R webapp:webapp buildout.cfg cgeo.cfg data entrypoint.sh  
  
USER webapp  
  
RUN python bin/buildout -v  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["demo"]  

