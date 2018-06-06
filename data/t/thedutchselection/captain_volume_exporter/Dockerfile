# NAME: Captain Container Exporter  
#  
# DESCRIPTION: This image exports a volume to a tarball and saves it. It can
also upload it to AWS S3.  
#  
# REQUIRED ENVS:  
# VOLUME (ie. "/home/postgresql/data")  
# TAR_BASE_FILENAME (ie. "postgresql_data" creates files called
postgresql_data_[timestamp].tar)  
# EXECUTION_TIME (ie. "16:00")  
#  
# OPTIONAL ENVS:  
# AWS_S3_ACCESS_KEY_ID (ie. "abcdabcd1234")  
# AWS_S3_SECRET_ACCESS_KEY (ie. "abcdabcd1234")  
# AWS_S3_BUCKET_NAME (ie. "tds-backups")  
# AWS_S3_BUCKET_REGION (ie. "eu-central-1")  
# AWS_S3_PATH (ie. "containers/jenkins_data/" ending with a slash)  
#  
# OTHER:  
#  
# To restore a volume use something like:  
# docker run --volumes-from postgresql_data --entrypoint "tar" -v
$(pwd):/backup thedutchselection/captain_volume_exporter xvf
/backup/backup.tar  
  
FROM thedutchselection/captain_services_base:latest  
MAINTAINER Gerard Meijer <g.meijer@thedutchselection.com>  
  
RUN \  
apk update && \  
apk add curl && \  
apk add docker && \  
apk add groff && \  
apk add less && \  
apk add python && \  
apk add py-pip && \  
pip install --upgrade --user awscli && \  
rm /var/cache/apk/*  
  
ADD files/scripts /usr/local/bin  
  
RUN chmod +x /usr/local/bin/*  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/run.sh"]  

