FROM ubuntu:14.04  
ENV PUPPETSERVER_JAVA_ARGS="-Xms2g -Xmx2g -XX:MaxPermSize=256m"  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
# RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
# && wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
# && wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
# && gpg --verify /usr/local/bin/gosu.asc \  
# && rm /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu \  
# && apt-get purge -y --auto-remove ca-certificates wget  
# Let's get Puppet Server installed  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install -y ruby-dev cron wget supervisor build-essential
libsqlite3-dev && \  
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb && \  
dpkg -i puppetlabs-release-pc1-trusty.deb && \  
apt-get update && \  
apt-get -y install puppetserver=2.3.0-1puppetlabs1 puppetdb-termini && \  
rm puppetlabs-release-pc1-trusty.deb  
  
# && \  
# /opt/puppetlabs/bin/puppetserver gem install jdbc-sqlite3 && \  
# /opt/puppetlabs/bin/puppetserver gem install CFPropertyList  
#apt-get -y install puppetserver=2.2.0-1puppetlabs1 puppetdb-
terminus=2.3.8-1puppetlabs1 && \  
ADD run.sh /run.sh  
  
RUN chmod +x /run.sh  
RUN sed -i s/START=no/START=yes/g /etc/default/puppet  
RUN mkdir -p /etc/cron.d  
ADD cron /etc/cron.d/  
ADD supervisord.conf /supervisord.conf  
VOLUME ["/etc/puppetlabs/puppet", "/etc/puppetlabs/puppetserver",
"/var/lib/puppet", "/etc/puppetlabs/code"]  
#ENTRYPOINT ["/run.sh"]  
EXPOSE 8140  
#COPY set_conf.sh /set_conf.sh  
#RUN chmod +x /set_conf.sh  
# CMD ['/set_conf.sh']  
#CMD ["/opt/puppetlabs/bin/puppetserver", "foreground"]  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c", "/supervisord.conf"]  
#CMD sh -c '/set_conf.sh && /opt/puppetlabs/bin/puppetserver foreground'  

