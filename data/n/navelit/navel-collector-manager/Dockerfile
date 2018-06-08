FROM perl:latest  
  
MAINTAINER Yoann Le Garff (le-garff-yoann) <pe.weeble@yahoo.fr>  
  
EXPOSE 8080 8443  
WORKDIR /tmp  
  
ADD https://github.com/navel-it/navel-installation-
scripts/archive/master.tar.gz .  
  
RUN \  
tar xvzf master.tar.gz && \  
bash navel-installation-scripts-master/navel-collector-manager.sh -12 master
&& \  
rm -Rf *  
  
USER navel-collector-manager  
  
ENTRYPOINT ["navel-collector-manager"]  
  
CMD ["/usr/local/etc/navel-collector-manager/meta.json"]  

