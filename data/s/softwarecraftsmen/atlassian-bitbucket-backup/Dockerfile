FROM java:8-jdk  
MAINTAINER Software Craftsmen GmbH und CoKG <office@software-craftsmen.at>  
  
ARG "version=unknown"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
ARG "vcs_ref=unknown"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="jenkins-backup" \  
org.label-schema.description="Jenkins Backup" \  
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
  
ARG http_proxy  
ARG https_proxy  
  
# Install postgresql  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update -y --no-install-recommends && \  
apt-get install -y postgresql-client && \  
rm -rf /var/lib/apt/lists/*  
  
# Install tools required by backup/restore (s3cmd, rsync)  
# Official s3cmd debian packages are outdated!  
RUN apt-get update && \  
apt-get -y install --no-install-recommends python-setuptools rsync && \  
rm -rf /var/lib/apt/lists/* && \  
wget --quiet
https://github.com/s3tools/s3cmd/releases/download/v1.6.1/s3cmd-1.6.1.zip && \  
unzip -q s3cmd-1.6.1.zip && \  
rm s3cmd-1.6.1.zip && \  
cd s3cmd-1.6.1 && python setup.py install && cd .. && rm -R s3cmd-1.6.1/  
  
# Install Groovy  
RUN wget --quiet https://dl.bintray.com/groovy/maven/apache-groovy-
binary-2.4.9.zip && \  
unzip -q -d/opt/ apache-groovy-binary-2.4.9.zip && \  
rm apache-groovy-binary-2.4.9.zip  
ENV GROOVY_HOME /opt/groovy-2.4.9  
#  
# Setup cron  
#  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends cron && \  
rm -rf /var/lib/apt/lists/*  
# Create the log file to be able to run tail  
ENV CRON_LOG=/var/log/cron.log  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN touch "${CRON_LOG}" && \  
chmod +x /docker-entrypoint.sh  
# Run the command on container startup  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Setup backup/restore scripts  
COPY /opt/backup/ /opt/backup/  
RUN chmod -R +x /opt/backup  

