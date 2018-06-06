# https://github.com/docker-library/docs/tree/master/node  
#http://www.ekito.fr/people/run-a-cron-job-with-docker/  
  
#FROM ubuntu:latest  
FROM node:0.10-onbuild  
  
COPY ./lib/phantomjs-1.9.7-linux-x86_64.tar.bz2
/tmp/phantomjs-1.9.7-linux-x86_64.tar.bz2  
  
#############################################################################  
# Env  
#############################################################################  
ENV PHANTOMJS_VERSION 1.9.7  
  
  
  
#############################################################################  
# Use to build with support for phantom js / pdf generation  
#############################################################################  
  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y cron vim git wget libfreetype6 libfontconfig bzip2 rsyslog
less && \  
mkdir -p /srv/var && \  
tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \  
ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \  
git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \  
ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \  
apt-get autoremove -y && \  
apt-get clean all  
  
#############################################################################  
# Add crontab file in the cron directory  
#############################################################################  
ADD hello-cron /etc/cron.d/hello-cron  
ADD gotprint-cron /etc/cron.d/gotprint-cron  
ADD claimcheck-cron /etc/cron.d/claimcheck-cron  
ADD inboxcbt-cron /etc/cron.d/inboxcbt-cron  
ADD inboxdbs-cron /etc/cron.d/inboxdbs-cron  
ADD ipupdate-cron /etc/cron.d/ipupdate-cron  
ADD cardrequestcheck-cron /etc/cron.d/cardrequestcheck-cron  
ADD cardrequestnotify-cron /etc/cron.d/cardrequestnotify-cron  
  
#############################################################################  
# added 12/26/2015 because cron was failing for security reasons but this file
works  
#############################################################################  
ADD cron-pam-fix /etc/pam.d/cron  
  
#############################################################################  
# Give execution rights on the cron jobs  
#############################################################################  
RUN chmod 0644 /etc/cron.d/hello-cron  
RUN chmod 0644 /etc/cron.d/gotprint-cron  
RUN chmod 0644 /etc/cron.d/claimcheck-cron  
RUN chmod 0644 /etc/cron.d/inboxcbt-cron  
RUN chmod 0644 /etc/cron.d/inboxdbs-cron  
RUN chmod 0644 /etc/cron.d/ipupdate-cron  
RUN chmod 0644 /etc/cron.d/cardrequestcheck-cron  
RUN chmod 0644 /etc/cron.d/cardrequestnotify-cron  
  
  
#############################################################################  
# Create the log file  
#############################################################################  
RUN touch /var/log/cron.log  
RUN touch /var/log/GotPrint.log  
RUN touch /var/log/checkForClaimFiles.log  
RUN touch /var/log/corp-inbox-monitor-cbt.log  
RUN touch /var/log/corp-inbox-monitor-dbs.log  
RUN touch /var/log/dbs_ip_update.log  
RUN touch /var/log/CardRequests.log  
RUN touch /var/log/CardRequestsNotifications.log  
  
  
#############################################################################  
# Add create our script folder  
#############################################################################  
RUN mkdir /etc/cbtscripts  
  
#############################################################################  
# Add crontab file in the cron directory  
#############################################################################  
ADD cbtstart.sh /etc/cbtscripts/cbtstart.sh  
  
#############################################################################  
# Give execution rights on startup script  
#############################################################################  
RUN chmod +rwx /etc/cbtscripts/cbtstart.sh  
  
WORKDIR /app  
#12/26/2015 NPM install runs twice - once triggered by the base image and once
because we run it  
ADD package-docker.json /app/package.json  
RUN npm install  
ADD . /app  
  
# we need cron running as well as the cbtProcessLauncher  
# cbtProcessLauncher should probably be the command we run  
  
CMD ["/etc/cbtscripts/cbtstart.sh"]

