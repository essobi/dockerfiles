FROM ograhl/job:latest  
  
  
### Installs  
# APT-GET Installs  
RUN apt-get update && \  
\  
echo "Installing..." && \  
apt-get install --no-install-recommends -y \  
ca-certificates \  
python-pip \  
wget \  
&& \  
\  
echo "Cleaning up..." && \  
rm -r /var/lib/apt/lists/*  
  
# PIP Installs  
ENV PIP_VERSION_INST="9.0.3"  
RUN echo "Installing (pip)..." && \  
pip install --upgrade pip==$PIP_VERSION_INST && \  
pip install setuptools && \  
pip install awscli  
  
### Copy files  
# Scripts  
COPY scripts/*.sh /  
  
### Final RUN steps  
# - /*.sh: Make executable  
RUN chmod 744 /*.sh  
  
### Define environment variables for job.sh script  
ENV \  
AWS_ACCESS_KEY_ID="please_set_environment_variable" \  
AWS_DEFAULT_REGION="us-east-1" \  
AWS_SECRET_ACCESS_KEY="please_set_environment_variable" \  
\  
PATHS_TO_BACKUP="/paths/to/backup" \  
\  
BACKUP_NAME="backup" \  
BACKUP_TAR_OPTION="" \  
S3_BUCKET="docker-backups.example.com" \  
\  
RESTORE="false" \  
RESTORE_FILE="" \  
RESTORE_TAR_OPTION=""  

