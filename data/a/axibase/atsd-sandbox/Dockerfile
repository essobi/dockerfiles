FROM ubuntu:16.04  
ENV version=latest LANG=en_US.UTF-8 DEPLOYMENT_TYPE=sandbox  
  
# metadata  
LABEL com.axibase.maintainer="ATSD Developers <dev-atsd@axibase.com>" \  
com.axibase.vendor="Axibase Corporation" \  
com.axibase.product="Axibase Time Series Database Sandbox" \  
com.axibase.code="ATSD Sandbox" \  
com.axibase.revision="${version}"  
  
# add initialization scripts  
COPY *init.sh /tmp/  
  
# install and configure  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com \--recv-keys
26AEE425A57967CFB323846008796A6514F3CB79 \  
&& apt-get update \  
&& LANG=C DEBIAN_FRONTEND=noninteractive apt-get install -y locales apt-utils
apt-transport-https \  
&& locale-gen en_US.UTF-8 \  
&& adduser --disabled-password --quiet --gecos "" axibase \  
&& echo "deb [arch=amd64] https://axibase.com/public/repository/deb/ ./" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
atsd wget unzip cron nano \  
iproute2 file python3 python3-pip python3-setuptools \  
&& pip3 install --upgrade pip && pip install atsd_client \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i '/.*hbase.cluster.distributed.*/{n;s/.*/ <value>false<\/value>/}'
/opt/atsd/hbase/conf/hbase-site.xml \  
&& sed -i 's/\\(max_tries_count=\\).\\+/\130/' /opt/atsd/bin/atsd-hbase.sh \  
&& wget -O /tmp/phantomjs.tar.gz
https://axibase.com/public/phantomjs-2.1.1-linux-x86_64.tar.gz \  
&& tar xzvf /tmp/phantomjs.tar.gz -C /opt/atsd \  
&& /tmp/atsd-init.sh \  
&& wget -O /tmp/collectd.deb https://github.com/axibase/atsd-collectd-
plugin/releases/download/5.7.2-7/collectd_ubuntu_16.04_amd64.deb \  
&& dpkg -i /tmp/collectd.deb \  
&& sed -i 's,atsd_url,tcp://localhost:8081,' /etc/collectd.conf \  
&& wget -P /tmp -e robots=off -r -nd https://axibase.com/public/axibase-
collector_latest.htm \  
&& tar xzvf /tmp/axibase-collector-*.tar.gz -C /opt/ \  
&& mkdir -p /opt/axibase-collector/exploded/webapp \  
&& unzip /opt/axibase-collector/lib/axibase-collector.war -d /opt/axibase-
collector/exploded/webapp \  
&& /tmp/collector-init.sh  
  
# jmx, network commands(tcp), network commands(udp), graphite pickle, UI/api
http, UI/api https, Collector https  
EXPOSE 1099 8081 8082/udp 8084 8088 8443 9443  
  
VOLUME ["/opt/atsd", "/opt/axibase-collector"]  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

