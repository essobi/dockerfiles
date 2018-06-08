FROM seeruk/java:openjdk-java8  
MAINTAINER Elliot Wright <hello@elliotdwright.com>  
  
ENV JENKINS https://hub.spigotmc.org/jenkins  
ENV SPIGOT_VERSION latest  
ENV SPIGOT_HEAP_INIT 2G  
ENV SPIGOT_HEAP_MAX 2G  
  
COPY ./provisioning/docker-entrypoint.sh /opt/mcbuild/docker-entrypoint.sh  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y git-core wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -d /opt/mcserver -u 1000 -m -s /bin/bash mcserver \  
&& mkdir -p /opt/mcserver \  
&& mkdir -p /opt/mcbuild \  
&& cd /opt/mcbuild \  
&& wget
${JENKINS}/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar \  
&& java -d64 -jar BuildTools.jar --rev ${SPIGOT_VERSION} \  
&& chown -R mcserver: /opt/mcbuild \  
&& chown -R mcserver: /opt/mcserver \  
&& chmod +x /opt/mcbuild/docker-entrypoint.sh  
  
USER mcserver  
  
EXPOSE 25565  
VOLUME /opt/mcserver  
WORKDIR /opt/mcserver  
  
ENTRYPOINT ["/opt/mcbuild/docker-entrypoint.sh"]  
  
CMD ["nogui"]  

