FROM redmine:3.4.4  
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"  
  
ENV REDMINE_PATH=/usr/src/redmine \  
REDMINE_LOCAL_PATH=/var/local/redmine  
  
# Install dependencies and plugins  
RUN apt-get update -q \  
&& apt-get install -y --no-install-recommends unzip graphviz vim python3-pip
cron rsyslog \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip3 install chaperone \  
&& mkdir -p ${REDMINE_LOCAL_PATH}/github /etc/chaperone.d/ \  
&& git clone -b RELEASE_0_7_0 https://github.com/tckz/redmine-
wiki_graphviz_plugin.git ${REDMINE_PATH}/plugins/wiki_graphviz_plugin \  
&& git clone -b Ver_0.3.0 https://github.com/masamitsu-
murase/redmine_add_subversion_links.git
${REDMINE_PATH}/plugins/redmine_add_subversion_links \  
&& git clone -b v2.2.0 https://github.com/koppen/redmine_github_hook.git
${REDMINE_PATH}/plugins/redmine_github_hook \  
&& git clone -b 0.0.2 https://github.com/bluezio/redmine_wiki_backlinks.git
${REDMINE_PATH}/plugins/redmine_wiki_backlinks \  
&& git clone -b 0.0.8 https://github.com/bdemirkir/sidebar_hide.git
${REDMINE_PATH}/plugins/sidebar_hide \  
&& git clone https://github.com/akiko-pusu/redmine_banner.git
${REDMINE_PATH}/plugins/redmine_banner \  
&& cd ${REDMINE_PATH}/plugins/redmine_banner \  
&& git checkout 5ae224156f188e9eb8fd9d84baeb3ff504541095 \  
&& cd .. \  
&& git clone -b 2.1.0 https://github.com/thorin/redmine_ldap_sync.git
${REDMINE_PATH}/plugins/redmine_ldap_sync \  
&& git clone https://github.com/eea/eea.redmine.theme.git
${REDMINE_PATH}/public/themes/eea.redmine.theme \  
&& chown -R redmine:redmine ${REDMINE_PATH} ${REDMINE_LOCAL_PATH}  
  
# Install gems  
RUN echo 'gem "dalli", "~> 2.7.6"' >> ${REDMINE_PATH}/Gemfile  
  
# Install eea cron tools  
COPY crons/ ${REDMINE_LOCAL_PATH}/crons  
COPY config/install_plugins.sh ${REDMINE_PATH}/install_plugins.sh  
COPY plugins.cfg ${REDMINE_PATH}/plugins.cfg  
  
COPY redmine_jobs /var/redmine_jobs.txt  
  
RUN sed -i '/#cron./c\cron.* \/proc\/1\/fd\/1' /etc/rsyslog.conf \  
&& sed -i 's/-\/var\/log\/syslog/\/proc\/1\/fd\/1/g' /etc/rsyslog.conf  
  
RUN echo "export REDMINE_PATH=$REDMINE_PATH\nexport
BUNDLE_PATH=$BUNDLE_PATH\nexport BUNDLE_APP_CONFIG=$BUNDLE_PATH\nexport
PATH=$BUNDLE_PATH/bin:$PATH" > ${REDMINE_PATH}/.profile \  
&& chown redmine:redmine ${REDMINE_PATH}/.profile \  
&& usermod -d ${REDMINE_PATH} redmine  
  
# Send Redmine logs on STDOUT/STDERR  
COPY config/additional_environment.rb
${REDMINE_PATH}/config/additional_environment.rb  
  
# Add email configuration  
COPY config/configuration.yml ${REDMINE_PATH}/config/configuration.yml  
  
COPY start_redmine.sh /start_redmine.sh  
RUN chmod 0766 /start_redmine.sh  
  
ENTRYPOINT ["/start_redmine.sh"]  
  
CMD []  

