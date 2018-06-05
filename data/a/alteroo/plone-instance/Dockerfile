FROM alteroo/plone-base  
MAINTAINER David Bain <david@alteroo.com>  
  
# default values are set upstream  
# ENV PASSWORD secret  
# ENV MAJORVERSION 4.3  
# ENV MINORVERSION 4.3.4  
# ENV TARGETDIR /opt/plone  
# ENV INSTANCENAME app  
# ENV INSTANCEDIR $TARGETDIR/$INSTANCENAME  
ADD instance.cfg $INSTANCEDIR/  
WORKDIR $INSTANCEDIR  
RUN bin/buildout -c instance.cfg  
  
CMD sed -i "s/INSTANCEDIR/$INSTANCEDIR/g"
parts/instance/etc/zope.conf;bin/instance console  
  
EXPOSE 8080  

