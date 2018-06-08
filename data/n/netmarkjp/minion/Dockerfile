FROM ubuntu:12.04  
MAINTAINER Toshiaki Baba <toshiaki@netmark.jp>  
  
## minion  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN echo "postfix postfix/main_mailer_type select Internet Site" | debconf-
set-selections  
RUN echo "postfix postfix/mailname string 127.0.0.1" | debconf-set-selections  
RUN apt-get -y install git build-essential python-virtualenv python-dev
mongodb-server rabbitmq-server curl libcurl4-openssl-dev stunnel4 debconf-
utils postfix vim tree unzip supervisor curl gunicorn sudo  
RUN useradd minion  
RUN echo 'Defaults:minion !requiretty' >> /etc/sudoers.d/minion ; echo 'minion
ALL = NOPASSWD: ALL' >> /etc/sudoers.d/minion ; chmod 400
/etc/sudoers.d/minion  
RUN git clone https://github.com/mozilla/minion.git /opt/minion  
RUN chown -R minion:minion /opt/minion  
RUN install -d -o minion -g minion /opt/minion ; install -d -o minion -g
minion /var/log/supervisor ; install -d -o minion -g minion
/opt/minion/scripts ; install -d -o minion -g minion /opt/minion/plugins  
RUN chmod a+x /opt/minion/setup.sh  
RUN cd /opt/minion && sudo -u minion ./setup.sh clone /opt/minion  
RUN cd /opt/minion && sudo -u minion ./setup.sh install /opt/minion  
RUN install -d -o minion -g minion /etc/minion  
ADD frontend.json /etc/minion/frontend.json  
RUN sed -i.bak "s/SECRET_VALUE/${RANDOM}${RANDOM}${RANDOM}${RANDOM}${RANDOM}/"
/etc/minion/frontend.json  
  
## skipfish plugin  
RUN sudo -u minion curl -o /opt/minion/plugins/skipfish.deb
http://launchpadlibrarian.net/126324272/skipfish_2.10b-1_amd64.deb  
RUN dpkg -i /opt/minion/plugins/skipfish.deb  
RUN sudo -u minion git clone https://github.com/mozilla/minion-skipfish-plugin
/opt/minion/plugins/minion-skipfish-plugin  
RUN cd /opt/minion/plugins/minion-skipfish-plugin && python
/opt/minion/plugins/minion-skipfish-plugin/setup.py install  
  
## nmap plugin  
RUN apt-get -y install nmap  
RUN sudo -u minion git clone https://github.com/mozilla/minion-nmap-plugin
/opt/minion/plugins/minion-nmap-plugin  
RUN cd /opt/minion/plugins/minion-nmap-plugin && python
/opt/minion/plugins/minion-nmap-plugin/setup.py install  
  
## supervisor  
RUN install -d /etc/supervisor ; install -d /etc/supervisor/conf.d  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD minion-backend.supervisor.conf /etc/supervisor/conf.d/minion-
backend.supervisor.conf  
ADD minion-plugin-worker.supervisor.conf /etc/supervisor/conf.d/minion-plugin-
worker.supervisor.conf  
ADD minion-scan-worker.supervisor.conf /etc/supervisor/conf.d/minion-scan-
worker.supervisor.conf  
ADD minion-state-worker.supervisor.conf /etc/supervisor/conf.d/minion-state-
worker.supervisor.conf  
ADD minion-frontend.supervisor.conf /etc/supervisor/conf.d/minion-
frontend.supervisor.conf  
ADD rabbitmq.supervisor.conf /etc/supervisor/conf.d/rabbitmq.supervisor.conf  
ADD mongod.supervisor.conf /etc/supervisor/conf.d/mongod.supervisor.conf  
RUN locale-gen en_US en_US.UTF-8  
RUN locale-gen ja_JP ja_JP.UTF-8  
  
## sshd  
RUN apt-get -y install openssh-server  
RUN echo 'minion:minion' |chpasswd  
RUN mkdir /var/run/sshd  
ADD sshd.supervisor.conf /etc/supervisor/conf.d/sshd.supervisor.conf  
  
EXPOSE 8080 4369 5672 51509 22  
CMD ["/usr/bin/supervisord"]  
  
##  
## after docker run, must init db by using ssh(minion/minion) or nsinit or
nsenter  
##  
## minion-db-init  
## minion-create-plan /opt/minion/minion-backend/plans/basic.plan  
## minion-create-plan /opt/minion/minion-backend/plans/skipfish.plan  
## minion-create-plan /opt/minion/minion-backend/plans/nmap.plan  
##  

