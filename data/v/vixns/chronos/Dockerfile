FROM openjdk:8-jdk  
  
ADD . /src  
  
RUN cd /src \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y apt-transport-https \  
&& echo "deb http://repos.mesosphere.com/debian stretch main" | tee -a
/etc/apt/sources.list.d/mesosphere.list \  
&& echo 'deb https://deb.nodesource.com/node_7.x stretch main' | tee
/etc/apt/sources.list.d/nodesource.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y --force-yes \  
systemd \  
mesos \  
maven \  
nodejs \  
scala \  
libcurl3-nss \  
&& ln -sf /usr/bin/nodejs /usr/bin/node \  
&& mvn -Dmaven.test.skip=true clean package \  
&& mkdir -p /chronos \  
&& mv target/chronos*jar /chronos/chronos.jar \  
&& mv bin/start.sh /entrypoint.sh \  
&& cd / \  
&& dpkg --purge maven nodejs scala \  
&& apt-get clean autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.m2 /src  
  
ENV PORT1=8080  
  
ENTRYPOINT ["/entrypoint.sh"]  

