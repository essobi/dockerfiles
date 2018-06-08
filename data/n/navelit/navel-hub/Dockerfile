FROM perl:latest  
  
MAINTAINER Yoann Le Garff (le-garff-yoann) <pe.weeble@yahoo.fr>  
  
EXPOSE 8080 8443  
WORKDIR /tmp  
  
ADD https://github.com/navel-it/navel-installation-
scripts/archive/master.tar.gz .  
  
RUN \  
tar xvzf master.tar.gz && \  
bash navel-installation-scripts-master/navel-hub.sh -1 master && \  
rm -Rf *  
  
USER navel-hub  
  
ENTRYPOINT ["hypnotoad"]  
  
CMD ["-f", "/opt/navel-hub/script/navel-hub"]  

