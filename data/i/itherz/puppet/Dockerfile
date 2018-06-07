FROM debian:jessie  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD sources.list /etc/apt/  
  
RUN echo "ru_RU.UTF-8 UTF-8" >>/etc/locale.gen && apt-get update && apt-get
install -y make build-essential locales && locale-gen && export
LC_ALL=ru_RU.UTF-8 && apt-get install -y wget && cd /tmp && \  
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb && dpkg -i
*.deb && \  
apt-get update && apt-get install -f && apt-get install -y libsqlite3-dev g++
ruby ruby-dev sudo postgresql postgresql-contrib git git-core net-tools perl
perl-base liberror-perl puppetserver puppetdb r10k activemq python-setuptools
puppetdb-termini mc at && \  
mkdir /usr/share/activemq/activemq-data && chmod 777 -R
/usr/share/activemq/activemq-data && \  
mkdir /var/run/activemq && chown activemq /var/run/activemq && chmod 755 -R
/var/run/activemq && chown activemq /var/lib/activemq/data/ && chmod 755
/var/lib/activemq/data/ && \  
sed -i "s/stomp1/localhost/g" /etc/puppetlabs/mcollective/client.cfg && sed -i
"s/stomp1/localhost/g" /etc/puppetlabs/mcollective/server.cfg && \  
/opt/puppetlabs/bin/puppetserver gem install deep_merge redis && \  
cd /opt/puppetlabs/puppet/bin && ./ruby gem install redis && \  
gem install redis bundler && \  
echo "Europe/Moscow" >/etc/timezone && dpkg-reconfigure tzdata && \  
apt-get install -y redis-server && \  
sed -i "s/daemonize yes/daemonize no/ig" /etc/redis/redis.conf && \  
sed -i "s/bind 127.0.0.1/bind 0.0.0.0/ig" /etc/redis/redis.conf && \  
mkdir /opt/puppetlabs/mcollective/plugins/mcollective && cd
/opt/puppetlabs/mcollective/plugins/mcollective && \  
git clone https://github.com/puppetlabs/mcollective-puppet-agent . && \  
mkdir -p /var/cache/r10k && ln -s /opt/puppetlabs/bin/puppet /usr/bin && ln -s
/opt/puppetlabs/bin/mco /usr/bin && ln -s /opt/puppetlabs/bin/facter /usr/bin
&& rm /etc/puppetlabs/puppet/puppet.conf && rm
/etc/puppetlabs/puppetdb/conf.d/jetty.ini && \  
cd /root && git clone https://github.com/ajf8/mcomaster && cd mcomaster &&
mkdir -p /opt/puppetlabs/mcollective/plugins/mcollective/registration && cp
mcollective/registration/meta.rb
/opt/puppetlabs/mcollective/plugins/mcollective/registration/ && \  
mkdir -p /opt/puppetlabs/mcollective/plugins/mcollective/agent && cp
mcollective/agent/* /opt/puppetlabs/mcollective/plugins/mcollective/agent && \  
mkdir -p /opt/puppetlabs/mcollective/plugins/mcollective/discovery && cp
mcollective/discovery/*
/opt/puppetlabs/mcollective/plugins/mcollective/discovery && \  
mkdir -p /var/lib/puppet/gitlab-webhook  
  
ADD gitlab-webhook-r10k.py /var/lib/puppet/gitlab-webhook  
  
#ENV REAKTOR_PUPPET_MASTERS_FILE="/root/masters.txt"  
#ENV PUPPETFILE_GIT_URL="git@github.com:example.org/puppetfile.git"  
ENV LANG "ru_RU.UTF-8"  
ENV LC_ALL "ru_RU.UTF-8"  
ENV LANGUAGE "ru_RU.UTF-8"  
ADD server.cfg /etc/puppetlabs/mcollective/  
ADD client.cfg /etc/puppetlabs/mcollective/  
  
ADD hiera.yaml /etc/puppetlabs/code/  
ADD r10k.agent.rb
/opt/puppetlabs/mcollective/plugins/mcollective/agent/r10k.rb  
ADD r10k.ddl /opt/puppetlabs/mcollective/plugins/mcollective/agent/r10k.rb  
ADD r10k.application.rb
/opt/puppetlabs/mcollective/plugins/mcollective/application/r10k.rb  
ADD puppet.conf /etc/puppetlabs/puppet/  
ADD puppetdb.conf /etc/puppetlabs/puppet/  
ADD puppet.conf /etc/puppet/  
ADD puppetdb.conf /etc/puppet/  
  
RUN mkdir /var/log/supervisor/ && /usr/bin/easy_install supervisor &&
/usr/bin/easy_install supervisor-stdout && /usr/bin/easy_install supervisor-
logging && sed -i 's/md5/trust/ig' /etc/postgresql/9.4/main/pg_hba.conf  
ADD run_puppet_db.sh /opt/puppetlabs/  
ADD run_puppet.sh /opt/puppetlabs/  
ADD supervisord.conf /etc/supervisord.conf  
ADD activemq.xml /etc/activemq/instances-enabled/mco/  
ADD log4j.properties /etc/activemq/instances-enabled/mco/  
ADD jetty.ini /etc/puppetlabs/puppetdb/conf.d  
ADD database.ini /etc/puppetlabs/puppetdb/conf.d  
  
VOLUME
["/etc/puppetlabs/puppet/ssl","/etc/puppetlabs/code/environments","/etc/puppetlabs/code/hieradata"]  
  
EXPOSE 8140 6163 8080 8081 6379 4570 7000  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

