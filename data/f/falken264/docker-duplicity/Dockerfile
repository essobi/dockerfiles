FROM phusion/baseimage:0.9.17  
MAINTAINER David Falk  
  
RUN apt-get update && \  
apt-get install -y wget ncftp python-pycryptopp lftp python-boto python-dev
python-setuptools librsync-dev build-essential openssh-client python-lockfile
python-pip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && \  
apt-get install -y expect postfix && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install paramiko  
  
RUN wget
https://code.launchpad.net/duplicity/0.7-series/0.7.05/+download/duplicity-0.7.05.tar.gz
&& \  
tar xzvf duplicity*  
  
RUN cd duplicity* && \  
python setup.py install  
  
RUN mkfifo /var/spool/postfix/public/pickup  
  
VOLUME /data  
VOLUME /root/.gnupg/  
VOLUME /root/.ssh/  
VOLUME /logs  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN chmod 777 /etc/ssh/ssh_config  
  
ADD setup.sh /etc/my_init.d/setup.sh  
RUN chmod a+x /etc/my_init.d/setup.sh  
  
ADD duplicity-runner.sh /usr/bin/duplicity-runner  
RUN chmod a+x /usr/bin/duplicity-runner  
  
ADD duplicity-restore.sh /usr/bin/duplicity-restore  
RUN chmod a+x /usr/bin/duplicity-restore  
  
ADD expect_ssh_fingerprint /usr/bin/expect_ssh_fingerprint  
RUN chmod a+x /usr/bin/expect_ssh_fingerprint  
  
#ADD prepare.sh /usr/bin/prepare  
#RUN chmod a+x /usr/bin/prepare  
# Add our crontab file  
ADD crons.conf /root/crons.conf  
  
# Use the crontab file  
RUN crontab /root/crons.conf  
  
# Start cron  
RUN cron  

