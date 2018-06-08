### Postgres 9.5 based on DEBIAN  
FROM postgres:9.5  
### Jira and Postgres vars  
ARG INIT_FILE=init-scripts/trainingdata.sql  
ARG JIRA_VERSION=software-7.8.0  
ARG DATABASE_TYPE=psql  
ARG JIRA_CONTEXT_PATH=/dev/jira-${JIRA_VERSION}-${DATABASE_TYPE}  
  
  
### Initial directories  
ARG INSTALL_DIR=/opt/atlassian/jira  
ARG HOME_DIR=/var/atlassian/jira  
ARG INIT_DIR=/docker-init  
ARG IMGDIR=/opt/atlassian/jira/atlassian-jira/images  
  
ENV POSTGRES_INITDB_ARGS="--lc-ctype=C --lc-collate=C --encoding=UTF8"  
ENV JIRA_MIN_MEM=512  
ENV JIRA_MAX_MEM=2048  
### OS preparation and package installation  
RUN apt-get update && apt-get install -y gettext wget curl build-essential
chrpath libssl-dev libxft-dev  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install  
  
### PhantomJS vars and installation  
ARG PHANTOM_JS=phantomjs-1.9.8-linux-x86_64  
  
RUN set -x \  
&& wget --progress=dot:mega
https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \  
&& tar xvjf $PHANTOM_JS.tar.bz2 \  
&& mv $PHANTOM_JS /usr/local/share \  
&& ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
### Sql init file/db update  
ADD $INIT_FILE prepare/init.sql  
ADD init-scripts/zzz-update-last.sh /docker-init/  
  
USER root  
  
### Initial setup along with database tests  
COPY ["/jira-config/response.varfile", "/"]  
COPY ["docker-entrypoint.sh", "/"]  
COPY ["db-config", "${INIT_DIR}/db"]  
COPY ["jira-config", "${INIT_DIR}/jira"]  
COPY ["filebeat.yml", "${INIT_DIR}/filebeat.yml"]  
  
### Jira download and install  
RUN set -x \  
&& wget --progress=dot:mega
https://www.atlassian.com/software/jira/downloads/binary/atlassian-
jira-${JIRA_VERSION}-x64.bin \  
&& chmod a+x atlassian-jira-${JIRA_VERSION}-x64.bin \  
&& ./atlassian-jira-${JIRA_VERSION}-x64.bin -q -varfile
${INIT_DIR}/jira/response.varfile \  
&& rm atlassian-jira-${JIRA_VERSION}-x64.bin \  
&& $INSTALL_DIR/bin/catalina.sh stop -force  
  
### Filebeat Setup  
RUN set -x \  
&& wget --progress=dot:mega
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.1.2-amd64.deb
\  
&& dpkg -i filebeat-6.1.2-amd64.deb  
  
### INSTALLING PLUGINS: BIGPICTURE, BIGPICTURE ENTERPRISE, BIGTEMPLATE, TEMPO
PLANNER  
RUN mkdir -p ${HOME_DIR}/plugins/installed-plugins  
RUN chmod -R 777 ${HOME_DIR}  
ADD
https://softwareplant.atlassian.net/wiki/download/attachments/79069239/devtool-1.0.1-jira7.jar
${HOME_DIR}/plugins/installed-plugins  
ADD
https://marketplace.atlassian.com/download/plugins/com.atlassian.labs.rest-
api-browser/version/30210 ${HOME_DIR}/plugins/installed-plugins/rest-api-
plugin.jar  
ADD
https://marketplace.atlassian.com/download/plugins/eu.softwareplant.bigpicture
${HOME_DIR}/plugins/installed-plugins/bigpicture.jar  
ADD
https://marketplace.atlassian.com/download/plugins/softwareplant.bigpictureenterprise
${HOME_DIR}/plugins/installed-plugins/bigpicture-enterprise.jar  
ADD
https://marketplace.atlassian.com/download/plugins/softwareplant.bigtemplate
${HOME_DIR}/plugins/installed-plugins/bigtemplate.jar  
ADD /plugins/* ${HOME_DIR}/plugins/installed-plugins/  
  
### SETS UP LOCALTIME  
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime  
  
### REPLACING IMAGES AND ICONS  
COPY ["/images/64jira.png", "${IMGDIR}/64jira.png"]  
COPY ["/images/BPE_logo_normal.png", "${IMGDIR}/icon-jira-logo.png"]  
#COPY ["/images/32jira.png", "${IMGDIR}/icons/favicon.png"]  
COPY ["/indexes/", "${HOME_DIR}/caches/indexes/"]  
  
### Exposing ports for Jira and Postgres  
EXPOSE 8080  
EXPOSE 8000  
EXPOSE 5432  
VOLUME ["$HOME_DIR", "$INSTALL_DIR", "$INIT_DIR"]  
  
WORKDIR $HOME_DIR  
  
RUN chmod a+x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

