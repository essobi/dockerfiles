#################################################################  
## UD HHVM  
##  
## docker build -t usabilitydynamics/hhvm:0.1.0 \--rm .  
##  
## * http://ryansechrest.com/2013/08/managing-file-and-folder-permissions-
when-deploying-with-git/  
##  
## @ver 0.2.1  
## @author potanin@UD  
#################################################################  
  
FROM dockerfile/nodejs  
MAINTAINER Usability Dynamics, Inc. "http://usabilitydynamics.com"  
USER root  
  
VOLUME /var/log  
VOLUME /var/www  
  
RUN \  
groupadd --gid 500 hipstack && \  
useradd --create-home --shell /bin/bash --groups adm,sudo --uid 500 -g
hipstack hipstack && \  
mkdir /home/hipstack/.ssh  
  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
export NODE_ENV=development && \  
wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - && \  
echo deb http://dl.hhvm.com/ubuntu trusty main | tee
/etc/apt/sources.list.d/hhvm.list && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install hhvm supervisor nano && \  
npm install --global forever mocha should chai grunt-cli express  
  
ADD bin /usr/local/src/hipstack/bin  
ADD lib /usr/local/src/hipstack/lib  
ADD static/etc /usr/local/src/hipstack/static/etc  
ADD package.json /usr/local/src/hipstack/package.json  
ADD readme.md /usr/local/src/hipstack/readme.md  
  
ADD static/etc/apache2/default.conf /etc/apache2/sites-enabled/default.conf  
ADD static/etc/supervisord.conf /etc/supervisor/supervisord.conf  
ADD static/etc/default/hipstack.sh /etc/default/hipstack  
ADD static/etc/init.d/hipstack.sh /etc/init.d/hipstack  
  
RUN \  
export NODE_ENV=production && \  
mkdir -p /etc/hipstack && \  
mkdir -p /etc/hipstack/ssl && \  
mkdir -p /var/lib/hipstack && \  
mkdir -p /var/log/hipstack && \  
mkdir -p /var/cache/hipstack && \  
mkdir -p /var/run/hipstack && \  
mkdir -p /var/run/supervisor && \  
mkdir -p /var/log/supervisor && \  
chgrp -R hipstack /var/lib/hipstack && \  
chgrp -R hipstack /var/www && \  
chmod g-w /var/www && \  
chmod g+s /var/www && \  
chgrp hipstack /var/log/hipstack && \  
chgrp hipstack /var/run/hipstack && \  
chgrp hipstack /var/cache/hipstack && \  
chgrp hipstack /tmp && \  
npm link /usr/local/src/hipstack  
  
RUN \  
npm cache clean && apt-get autoremove && apt-get autoclean && apt-get clean &&
\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod +x /etc/init.d/**  
  
EXPOSE 80  
  
ENV NODE_ENV production  
ENV PHP_ENV production  
  
WORKDIR /home/hipstack  
  
ENTRYPOINT [ "/usr/local/bin/hipstack.entrypoint" ]  
CMD [ "/bin/bash" ]  
  

