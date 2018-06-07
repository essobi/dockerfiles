FROM ubuntu:xenial  
LABEL maintainer="Lukasz Karolewski"  
RUN apt-get update && apt-get install -y wget  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add -  
  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list'  
RUN apt-get update && apt-get install -y python-pip postgresql-client-9.6 cron  
RUN pip install awscli  
  
ENV DIR /home/pg-dockup  
ENV LOCAL_BACKUP_DIR $DIR/local-backup  
  
RUN mkdir $DIR  
WORKDIR $DIR  
COPY . $DIR  
RUN chmod 755 $DIR/*.sh  
  
VOLUME $LOCAL_BACKUP_DIR  
  
ENV BACKUP_NAME pg_dump  
ENV AWS_S3_CP_OPTIONS --sse AES256  
ENV PG_DUMP_OPTIONS --verbose  
  
CMD ["./run.sh"]  

