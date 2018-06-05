FROM redmatter/cron  
  
MAINTAINER Dino.Korah@RedMatter.com  
  
ENV TZ="Europe/London" \  
BAMBOO_USER=daemon \  
BAMBOO_GROUP=daemon \  
BAMBOO_BACKUP_HOME=/app/atlassian/bamboo/backup \  
BAMBOO_BACKUP_USER=backup \  
BAMBOO_BACKUP_PASS=letmein \  
BAMBOO_URL=http://bamboo \  
MYSQL_HOST=mysql \  
MYSQL_DATABASE=bamboo \  
MYSQL_USER=atlbamboo \  
MYSQL_PASSWORD=letmein \  
PRESERVE_ENV_VARS="MYSQL_HOST MYSQL_DATABASE MYSQL_USER MYSQL_PASSWORD \  
RUN_USER RUN_GROUP \  
BAMBOO_USER BAMBOO_GROUP \  
BAMBOO_BACKUP_USER BAMBOO_BACKUP_PASS \  
BAMBOO_URL BAMBOO_BACKUP_EXCLUDE \  
BAMBOO_BACKUP_HOME BACKUP_ARCHIVE_TYPE \  
AWS_ACCESS_KEY AWS_SECRET_KEY AWS_S3_BUCKET AWS_S3_BUCKET_PATH \  
GNUPGHOME GPG_MODE GPG_RECIPIENT GPG_PASSPHRASE \  
"  
ENV BAMBOO_BACKUP_LOG=${BAMBOO_BACKUP_HOME}/log/bamboo-backup.log \  
# semantics to work with cron base image  
RUN_USER=${BAMBOO_USER} \  
RUN_GROUP=${BAMBOO_GROUP} \  
GNUPGHOME=${BAMBOO_BACKUP_HOME}/.gnupg  
  
# pull in the bits we need for the build  
ADD https://github.com/redmatter/atlassian-bamboo-diy-backup/archive/1.0.1.zip
/tmp/files.zip  
COPY bamboo.diy-backup.vars.sh rotate-log.sh s3sync.sh s3cfg.ini run-backup.sh
/tmp/  
  
RUN ( \  
export DEBIAN_FRONTEND=noninteractive; \  
export BUILD_DEPS="unzip"; \  
export APP_DEPS="tar mysql-client jq rsync curl ca-certificates s3cmd"; \  
  
# so that each command can be seen clearly in the build output  
set -e -x; \  
  
# update to pull package list from apt sources  
apt-get update; \  
apt-get install --no-install-recommends -y $BUILD_DEPS $APP_DEPS ; \  
  
mkdir -p ${BAMBOO_BACKUP_HOME} ; \  
cd ${BAMBOO_BACKUP_HOME} ; \  
  
mkdir -p /bamboo-backups log bin archives tmp/bamboo-db tmp/bamboo-home
/var/atlassian/application-data/bamboo ; \  
touch ${BAMBOO_BACKUP_LOG} ; \  
  
# extract the archive, apply patch and add the config  
unzip -j -d bin /tmp/files.zip ; \  
rm /tmp/files.zip ; \  
mv /tmp/bamboo.diy-backup.vars.sh /tmp/rotate-log.sh /tmp/s3sync.sh /tmp/run-
backup.sh bin ; \  
  
# create user with crontab capability  
cron-user add -u $BAMBOO_USER -g $BAMBOO_GROUP; \  
  
# set correct permissions  
chown -R ${BAMBOO_USER}:${BAMBOO_GROUP} . /var/atlassian/application-
data/bamboo /bamboo-backups ; \  
chmod -R go-rwx /bamboo-backups log bin tmp archives
/var/atlassian/application-data/bamboo ; \  
  
# move s3 configs to BAMBOO_BACKUP_HOME  
mv /tmp/s3cfg.ini .; \  
  
# remove packages that we don't need  
apt-get remove -y $BUILD_DEPS ; \  
apt-get autoremove -y ; \  
apt-get clean; \  
rm -rf /var/lib/apt/ /var/lib/dpkg/ /var/lib/cache/ /var/lib/log/; \  
)  
  
WORKDIR ${BAMBOO_BACKUP_HOME}  
  
VOLUME [ "/bamboo-backups", "${BAMBOO_BACKUP_HOME}/log",
"/var/atlassian/application-data/bamboo" ]  
  
USER ${BAMBOO_USER}  

