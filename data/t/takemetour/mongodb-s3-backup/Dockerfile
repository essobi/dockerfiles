FROM slafs/python-ubuntu:2.7-wily  
  
MAINTAINER PanJ  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN apt-get update --fix-missing  
RUN apt-get install -y cron mongodb-org-tools mongodb-org-shell  
RUN pip install awscli  
RUN service cron start  
  
ADD ./backup.sh /mongodb-s3-backup/backup.sh  
ADD ./cron-setup.sh /mongodb-s3-backup/cron-setup.sh  
WORKDIR /mongodb-s3-backup  
RUN chmod +x /mongodb-s3-backup/backup.sh  
RUN chmod +x /mongodb-s3-backup/cron-setup.sh  
  
ENTRYPOINT ["/bin/sh"]  
CMD ["./cron-setup.sh"]  

