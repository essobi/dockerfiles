FROM rodrigozc/consul-filebeat-agents:1.0.2  
LABEL author.name="Rodrigo Zampieri Castilho"  
LABEL author.email="rodrigo.zampieri@gmail.com"  
LABEL repository.url="https://bitbucket.org/rcastilho/jdk8-application"  
  
ENV APPLICATION_DEFAULT_NAME "jdk8-application"  
WORKDIR /app  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends gnupg2 dirmngr \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
RUN mkdir -p /app/data \  
&& mkdir -p /app/logs \  
&& mkdir -p /usr/share/man/man1 \  
&& mkdir -p /usr/share/binfmts \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y --no-install-recommends oracle-java8-installer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
ADD app.jar app.jar  
ADD application.ctmpl application.ctmpl  
ADD application.yml application.yml  
ADD consul-template/1-consul-template.list /etc/consul-template/  
ADD consul/service.ctmpl /etc/consul/  
ADD consul/service.json /etc/consul/  
ADD run/application.sh /docker/run/  

