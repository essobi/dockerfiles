FROM ograhl/job:latest  
  
  
### Installs  
# APT-GET Installs  
RUN apt-get update && \  
\  
echo "Installing..." && \  
apt-get install --no-install-recommends -y \  
ca-certificates \  
mysql-client \  
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
AWS_SECRET_ACCESS_KEY="please_set_environment_variable" \  
\  
EXCLUDE_DATABASES="Database,information_schema,performance_schema,sys" \  
S3_BUCKET="mysql-backup.example.com" \  
S3_PATH="mysql" \  
\  
MYSQL_HOST="mysql" \  
MYSQL_PORT="3306" \  
MYSQL_USER="root" \  
MYSQL_PASS="" \  
\  
RESTORE="false" \  
RESTORE_DATABASE="" \  
RESTORE_DB_CHARSET="utf8" \  
RESTORE_DB_COLLATION="utf8_bin"  

