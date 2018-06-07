FROM redmine:3.4.4  
LABEL maintainer="<informea@eaudeweb.ro>"  
  
ENV REDMINE_PATH=/usr/src/redmine \  
REDMINE_LOCAL_PATH=/var/local/redmine  
  
# Install dependencies and plugins  
RUN apt-get update -q \  
&& apt-get install -y --no-install-recommends cron unzip netcat-traditional
vim curl python3-pip build-essential python3-dev imagemagick\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install --upgrade setuptools \  
&& pip3 install PyYAML ruamel.yaml  
  
COPY plugins/* ${REDMINE_LOCAL_PATH}/plugins/  
  
RUN mkdir -p ${REDMINE_LOCAL_PATH}/github \  
&& mkdir -p ${REDMINE_LOCAL_PATH}/scripts \  
&& mkdir -p ${REDMINE_LOCAL_PATH}/backup \  
&& cd ${REDMINE_PATH}/plugins \  
&& git clone \--branch v2.2.0
https://github.com/koppen/redmine_github_hook.git \  
# && git clone --branch 1.0.9 https://framagit.org/infopiiaf/redhopper.git \  
# && git clone https://github.com/Ilogeek/redmine_issue_dynamic_edit.git \  
&& git clone https://github.com/foton/redmine_watcher_groups.git \  
&& git clone https://github.com/akiko-pusu/redmine_banner.git \  
&& git clone https://github.com/paginagmbh/redmine_silencer.git \  
&& git clone https://github.com/paginagmbh/redmine_lightbox2.git \  
&& git clone https://github.com/rgtk/redmine_impersonate.git \  
&& git clone https://github.com/rgtk/redmine_editauthor.git \  
&& git clone https://github.com/GEROMAX/redmine_subtask_list_accordion.git \  
&& git clone https://github.com/RCRM/redmine_checklists.git \  
&& git clone https://github.com/RCRM/redmine_agile.git \  
&& git clone https://github.com/RCRM/redmine_people.git \  
&& cd ${REDMINE_PATH} \  
&& gem install bundler --pre \  
&& chown -R redmine:redmine ${REDMINE_PATH} ${REDMINE_LOCAL_PATH} \  
&& unzip -d ${REDMINE_PATH}/public/themes -o
${REDMINE_LOCAL_PATH}/plugins/edw-theme.zip \  
&& unzip -d ${REDMINE_PATH}/public/themes -o
${REDMINE_LOCAL_PATH}/plugins/informea-theme.zip  
  
COPY entrypoint.sh scripts/receive_imap.sh scripts/update-repositories.sh
scripts/update_configuration.py ${REDMINE_LOCAL_PATH}/scripts/  
COPY crontab ${REDMINE_LOCAL_PATH}/  
  
WORKDIR $REDMINE_PATH  
ADD
http://www.redmine.org/attachments/download/18944/allow_watchers_and_contributers_access_to_issues_3.4.2.patch
\  
http://www.redmine.org/attachments/download/20075/redmine_3_4_log_time_for_others.patch
\  
patches/imap_scan_multiple_folders.patch \  
${REDMINE_PATH}/  
RUN patch -p0 < allow_watchers_and_contributers_access_to_issues_3.4.2.patch \  
&& patch -p0 < redmine_3_4_log_time_for_others.patch \  
&& patch -p0 < imap_scan_multiple_folders.patch  
  
ENTRYPOINT ["/var/local/redmine/scripts/entrypoint.sh"]  
CMD []  

