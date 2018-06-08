FROM python:2-stretch  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y rsyslog cron curl virtuoso-
opensource-6.1-bin \  
&& apt-get clean \  
&& pip install pysolr \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i '/#cron./c\cron.* \/proc\/1\/fd\/1' /etc/rsyslog.conf \  
&& git config --global user.email "scoreboard@digital-agenda-data.eu" \  
&& git config --global user.name "Digital Agenda Data"  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["cron", "-f"]  
  

