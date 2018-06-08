FROM debian:jessie  
MAINTAINER Stefan Fuchs  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the version you want of Dokuwiki  
ENV DOKUWIKI_VERSION 2018-04-22a  
ENV DOKUWIKI_CSUM 18765a29508f96f9882349a304bffc03  
  
# Update & install packages & cleanup afterwards  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install wget lighttpd php5-cgi php5-gd php5-curl php5-ldap && \  
apt-get -y install unzip openjdk-7-jre-headless graphviz && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
# Download & check & deploy dokuwiki & cleanup  
RUN wget -q -O /dokuwiki.tgz
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" &&
\  
if [ "$DOKUWIKI_CSUM" != "$(md5sum /dokuwiki.tgz | awk '{print($1)}')" ];then
echo "Wrong md5sum of downloaded file!"; exit 1; fi && \  
mkdir /dokuwiki && \  
tar -zxf dokuwiki.tgz -C /dokuwiki --strip-components 1 && \  
rm dokuwiki.tgz && \  
cd /dokuwiki/lib/plugins && \  
wget -q https://github.com/Andreone/dokuwiki_plantuml/archive/master.zip &&
unzip master.zip && mv dokuwiki_plantuml-master plantuml && rm master.zip && \  
mkdir plantuml/local && wget -O plantuml/local/plantuml.jar -q
https://sourceforge.net/projects/plantuml/files/plantuml.jar && \  
wget -q https://github.com/samuelet/indexmenu/archive/master.zip && unzip
master.zip && mv indexmenu-master/ indexmenu && rm master.zip && \  
wget -q https://github.com/samwilson/dokuwiki-plugin-
addnewpage/archive/master.zip && unzip master.zip && mv dokuwiki-plugin-
addnewpage-master addnewpage && rm master.zip && \  
wget -q https://github.com/cosmocode/edittable/archive/master.zip && unzip
master.zip && mv edittable-master/ edittable && rm master.zip && \  
wget -q https://github.com/leibler/dokuwiki-plugin-todo/archive/master.zip &&
unzip master.zip && mv dokuwiki-plugin-todo-master/ todo && rm master.zip && \  
wget -q https://github.com/jdehaan/dokuwiki-plugin-bpmnio/archive/master.zip
&& unzip master.zip && mv dokuwiki-plugin-bpmnio-master bpmnio && rm
master.zip && \  
wget -q https://github.com/michitux/dokuwiki-plugin-move/archive/master.zip &&
unzip master.zip && mv dokuwiki-plugin-move-master/ move && rm master.zip && \  
wget -q https://github.com/littleiffel/dokuwiki-slack-
integration/archive/master.zip && unzip master.zip && mv dokuwiki-slack-
integration-master slacknotifier && rm master.zip && \  
wget -q https://github.com/tillbiskup/dokuwiki-caption/archive/master.zip &&
unzip master.zip && mv dokuwiki-caption-master/ caption && rm master.zip  
  
  
# Configure plantuml for local rendering  
ADD plantuml/default.php /dokuwiki/lib/plugins/plantuml/conf/default.php  
# Set up ownership  
RUN chown -R www-data:www-data /dokuwiki  
  
# Configure lighttpd  
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
EXPOSE 80  
VOLUME ["/dokuwiki/data/", "/dokuwiki/conf/", "/dokuwiki/lib/tpl/"]  
  
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

