FROM softwarecraftsmen/cron:1.0.2  
MAINTAINER Software Craftsmen GmbH und CoKG <office@software-craftsmen.at>  
  
ARG version="unknown"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
ARG vcs_ref="unknown"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="sonarqube-backup" \  
org.label-schema.description="sonarqube-backup" \  
org.label-schema.usage="${vcs_url}" \  
org.label-schema.url="${vcs_url}" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$vcs_ref \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date  
  
RUN if [ ! "${http_proxy}" = "" ] ; then echo "Acquire::http::Proxy
\"${http_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "Acquire::https::Proxy
\"${https_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${http_proxy}" = "" ] ; then echo "http_proxy=${http_proxy}" >>
/etc/wgetrc; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "https_proxy=${https_proxy}" >>
/etc/wgetrc; fi  
  
# Install postgresql client, other tools  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget gnupg2  
  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >
/etc/apt/sources.list.d/pgdg.list && \  
wget --no-check-certificate --quiet -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add - && \  
apt-get update && \  
apt-get install -y --no-install-recommends postgresql-client unzip python-
setuptools s3cmd && \  
rm -rf /var/lib/apt/lists/*  
  
COPY backupmedia/ backupmedia/  
RUN chmod +x backupmedia/fs/*.sh backupmedia/s3/*.sh  
  
COPY backup.sh backup.sh  
COPY create-archive.sh create-archive.sh  
COPY restore.sh restore.sh  
COPY apply-archive.sh apply-archive.sh  
COPY restore-exclude restore-exclude  
COPY parsearguments.sh parsearguments.sh  
COPY cron-backup.sh cron-backup.sh  
COPY cron-setup.sh cron-setup.sh  
RUN chmod +x backup.sh create-archive.sh restore.sh apply-archive.sh cron-
setup.sh cron-backup.sh  

