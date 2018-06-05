FROM postgres:9.4.1  
MAINTAINER Hortonworks  
  
ENV REPONAME cloudbreak-autoscale-db  
ENV DBNAME pcdb  
ENV VERSION 1.10.0-rc.12  
ENV BACKUP_TGZ /initdb/$DBNAME-$VERSION.tgz  
  
ADD
https://github.com/hortonworks/docker-${REPONAME}/releases/download/v${VERSION}/${DBNAME}-${VERSION}.tgz
$BACKUP_TGZ  
ADD /start /  
  
ENTRYPOINT [ "/start" ]  
CMD ["postgres"]  

