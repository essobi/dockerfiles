FROM debian:jessie-slim  
MAINTAINER Rodrigo Zampieri Castilho <rodrigo.zampieri@gmail.com>  
  
ENV LC_ALL "pt_BR.UTF-8"  
ENV LANG "pt_BR.UTF-8"  
ENV LANGUAGE "pt_BR.UTF-8"  
ENV FILEBEAT_VERSION "5.4.0"  
ENV CONSUL_VERSION "0.8.3"  
ENV CONSUL_SERVER "consul-server"  
ENV CONSUL_INTERFACE "eth0"  
  
WORKDIR /app  
  
RUN mkdir -p /app/data \  
&& mkdir -p /app/logs \  
&& mkdir -p /opt/consul/data \  
&& mkdir -p /opt/consul/config \  
&& mkdir -p /usr/share/man/man1 \  
&& mkdir -p /usr/share/binfmts \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
EEA14886 \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y \--no-install-recommends oracle-java8-installer locales
unzip \  
&& echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen pt_BR.UTF-8 \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/* \  
# Filebeat Configuration  
&& wget \--no-check-certificate
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
\  
&& tar -zxvf /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz \  
&& mv /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat
/usr/bin/filebeat \  
&& mv /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat.template-
es2x.json /app \  
&& mv /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64/filebeat.template.json
/app \  
&& chmod +x /usr/bin/filebeat \  
&& rm -Rf /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64 \  
&& rm -Rf /app/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz \  
# Consul Configuration  
&& wget \--no-check-certificate
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
\  
&& unzip /app/consul_${CONSUL_VERSION}_linux_amd64.zip \  
&& mv /app/consul /usr/bin/consul \  
&& chmod +x /usr/bin/consul \  
&& rm /app/consul_${CONSUL_VERSION}_linux_amd64.zip  
  
ADD app.jar app.jar  
ADD application.yml application.yml  
ADD filebeat.yml /app/  
ADD docker-entrypoint.sh /app/  
  
ENTRYPOINT ["sh","docker-entrypoint.sh"]  

