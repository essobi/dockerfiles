FROM debian:jessie  
  
MAINTAINER Bastian Lemke <bastian@konschtanz.de>  
  
# Set correct environment variables  
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
RUN apt-get update -q  
RUN apt-get install -qy ssh supervisor cron  
RUN apt-get install -qy rsyslog postgresql-client  
RUN apt-get install -qy curl cpio  
  
ADD
https://download.code42.com/installs/linux/install/CrashPlan/CrashPlan_4.7.0_Linux.tgz
/tmp/CrashPlan.tgz  
RUN cd /tmp && \  
tar xf CrashPlan.tgz && \  
cd crashplan-install && \  
sed -i 's/^more /: /g' install.sh && \  
(echo; echo; echo yes; echo ; echo y; echo; echo /inbound-backups; echo y;
echo; echo; echo y; echo) | ./install.sh && \  
cd /usr/local/crashplan && \  
sleep 10 && \  
sed -i
's/<serviceHost>127.0.0.1<\/serviceHost>/<serviceHost>0.0.0.0<\/serviceHost>/g'
/usr/local/crashplan/conf/my.service.xml && \  
mv /usr/local/crashplan/conf /usr/local/crashplan/conf.default && \  
ln -s /config/conf /usr/local/crashplan/conf && \  
mv /usr/local/crashplan/log /usr/local/crashplan/log.default && \  
ln -s /config/log /usr/local/crashplan/log && \  
mv /var/lib/crashplan /var/lib/crashplan.default && \  
ln -s /config/crashplan /var/lib/crashplan && \  
rm -rf /tmp/CrashPlan.tgz /tmp/crashplan-install  
  
# install scripts & crontab for backup job  
COPY bin/start_cron.sh /usr/bin/start_cron.sh  
COPY bin/start_crashplan.sh /usr/bin/start_crashplan.sh  
COPY bin/cron_task /usr/bin/cron_task  
COPY bin/dump_postgres /usr/bin/dump_postgres  
  
COPY config/crontab /etc/cron.d/dump_postgres  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN chmod 0644 /etc/cron.d/dump_postgres  
RUN touch /var/log/cron.log  
RUN mkdir /var/run/sshd  
  
VOLUME ["/config"]  
VOLUME ["/inbound-backups"]  
VOLUME ["/data"]  
VOLUME ["/restore"]  
VOLUME ["/root/.ssh"]  
EXPOSE 22 4242 4243  
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf  

