FROM cogniteev/flume:1.6.0  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$arch" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$arch.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# install Docker engine, to retrieve the container name  
RUN apt-get update \  
&& apt-get install -y apt-transport-https ca-certificates \  
&& apt-key adv \  
\--keyserver hkp://p80.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D \  
&& echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' \  
> /etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y docker-engine  
  
ADD conf/* /var/src/agent/conf/  
ADD scripts/* /var/src/scripts/  
  
ENV AGENT_ROOT_DIR=/var/src/agent  
ENV AGENT_CONFIG_DIR=${AGENT_ROOT_DIR}/conf  
ONBUILD RUN mkdir -p /var/src/agent/extra-jars/  
ONBUILD ADD extra-jars/* /var/src/agent/extra-jars/  
ONBUILD ADD extra-src /var/src/agent/extra-src/  
ONBUILD RUN /var/src/scripts/10-build-extra-src  
ONBUILD ADD conf /var/src/agent/conf  
  
ENTRYPOINT ["/var/src/scripts/20-start-agent"]  

