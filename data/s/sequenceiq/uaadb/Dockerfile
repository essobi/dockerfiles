FROM postgres:9.4.4  
ENV DBNAME uaadb  
ENV VERSION 2.7.1  
ENV BACKUP_TGZ /initdb/$DBNAME-$VERSION.tgz  
  
ADD
https://github.com/sequenceiq/docker-${DBNAME}/releases/download/v${VERSION}/${DBNAME}-${VERSION}.tgz
$BACKUP_TGZ  
ADD /start /  
  
ENTRYPOINT [ "/start" ]  
CMD ["postgres"]  

