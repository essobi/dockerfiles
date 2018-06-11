FROM wetransform/dockup:latest  
MAINTAINER Simon Templer <simon@wetransform.to>  
  
# install MongoDB shell & tools  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-get update && \  
apt-get install -y mongodb-org-shell mongodb-org-tools  
  
ADD /scripts /dockup/  
RUN chmod 755 /dockup/*.sh  
  
ENV PATHS_TO_BACKUP /dockup/mongodump  
ENV MONGO_BACKUP_NAME mongodump  
ENV BEFORE_BACKUP_CMD ./mongodump.sh  
ENV AFTER_BACKUP_CMD ./mongoclean.sh  
ENV AFTER_RESTORE_CMD ./mongorestore.sh  
ENV MONGODB_HOST mongodb  
ENV MONGODB_PORT 27017  

