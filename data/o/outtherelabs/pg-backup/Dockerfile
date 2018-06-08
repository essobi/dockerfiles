FROM centos/postgresql-95-centos7  
MAINTAINER Julian Tescher "julian@outtherelabs.com"  
USER root  
  
# Install AWS SDK  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install python-pip && \  
pip install awscli && \  
yum -y remove python-pip && \  
yum clean all  
  
ENV POSTGRESQL_DATABASE **None**  
ENV POSTGRESQL_HOST **None**  
ENV POSTGRESQL_PORT 5432  
ENV POSTGRESQL_USER **None**  
ENV POSTGRESQL_PASSWORD **None**  
ENV POSTGRESQL_EXTRA_OPTS ''  
ENV AWS_ACCESS_KEY_ID **None**  
ENV AWS_SECRET_ACCESS_KEY **None**  
ENV AWS_DEFAULT_REGION us-west-2  
ENV S3_BUCKET **None**  
ENV S3_PATH 'backups'  
ADD backup.sh backup.sh  
  
RUN mkdir /var/backups && chmod g+rw /var/backups  
  
VOLUME /var/backups  
  
CMD ["sh", "backup.sh"]  

