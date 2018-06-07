#  
# Image used to publish the official Ceylon distribution to a Herd server  
#  
FROM ceylon/ceylon:latest-onbuild  
  
MAINTAINER Tako Schotanus <tako@ceylon-lang.org>  
  
LABEL org.ceylon-lang.dockerfile.description="Image used to publish the
official Ceylon distribution to a Herd server" \  
org.ceylon-lang.dockerfile.vendor="RedHat" \  
org.ceylon-lang.dockerfile.version="1.0"  
  
USER root  
RUN mkdir /output && \  
touch /output/.novolume && \  
chown -R ceylon:0 /output  
VOLUME /output  
USER ceylon  
  
ENTRYPOINT ["/app/publish.sh"]  
CMD []  
  

