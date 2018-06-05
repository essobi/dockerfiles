FROM ahilsend/duplicity  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ENV VERSION="0.0.1" \  
BACKUP_DIR=/backup  
  
LABEL maintainer="Andre.Hilsendeger@gmail.com" \  
name="heketi-backup" \  
version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="heketi-backup" \  
org.label-schema.vcs-url="https://github.com/ahilsend/hekteti-backup-
docker.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0" \  
org.label-schema.version=$VERSION  
  
COPY heketi-s3-backup.py /heketi-s3-backup.py  
  
RUN set -ex && \  
yum update -y && \  
yum install -y \  
glusterfs-fuse \  
python-pip && \  
pip install heketi && \  
yum remove -y \  
python-pip && \  
chmod +x /heketi-s3-backup.py  
  
CMD [ "/heketi-s3-backup.py" ]  

