FROM jordan/icinga2:latest  
  
RUN buildDeps=" \  
git \  
python-setuptools \  
" \  
&& wget "https://raw.githubusercontent.com/nisabek/icinga2-slack-
notifications/master/reprepro/pool/main/i/icinga2-slack-
notifications/icinga2-slack-notifications_1.0.4_all.deb" \  
&& dpkg -i icinga2-slack-notifications_1.0.4_all.deb \  
&& apt-get update && apt-get install -y jq $buildDeps --no-install-recommends
\  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/hannseman/hipsaint.git /opt/hipsaint \  
&& bash -c "cd /opt/hipsaint/ && python setup.py install" \  
&& apt-get purge -y \--auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
&& rm -r /opt/hipsaint/  
  
COPY hipsaint.conf /etc/icinga2.dist/conf.d/  
COPY hipchat* /etc/icinga2.dist/scripts/  
COPY setup.conf /etc/supervisor/conf.d/  
COPY config.sh /opt/setup/  
  
  
RUN mv /etc/icinga2/conf.d/slack-notifications/ /etc/icinga2.dist/conf.d/ \  
&& rm -r /etc/icinga2/conf.d \  
&& chown nagios /etc/icinga2.dist/scripts/hipchat* \  
&& chown nagios /etc/icinga2.dist/conf.d/slack-notifications/ \  
&& chmod +x /etc/icinga2.dist/scripts/hipchat* \  
&& rm /etc/icinga2.dist/conf.d/services.conf  

