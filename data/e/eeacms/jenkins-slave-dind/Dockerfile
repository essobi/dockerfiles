FROM eeacms/jenkins-slave:3.12  
  
ENV DOCKER_VERSION=1.12.6 \  
DOCKER_COMPOSE_VERSION=1.20.0 \  
DOCKER_COMPOSE_MD5=80b6349a390ef3a58250f892fb0cb3c1 \  
CLAIR_SCANNER_VERSION=v7  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends apt-transport-https ca-
certificates software-properties-common \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends docker-engine=$DOCKER_VERSION*
\  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -o /bin/docker-compose -SL
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-Linux-x86_64 \  
&& echo "$DOCKER_COMPOSE_MD5 /bin/docker-compose" | md5sum -c \- \  
&& chmod +x /bin/docker-compose \  
&& curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" \  
&& python /tmp/get-pip.py \  
&& pip install j2cli \  
&& curl -L -o /usr/bin/clair-scanner https://github.com/arminc/clair-
scanner/releases/download/$CLAIR_SCANNER_VERSION/clair-scanner_linux_amd64 \  
&& chmod 777 /usr/bin/clair-scanner  
  
COPY ini/settings.xml.j2 /tmp/settings.xml.j2  
COPY scripts/scan_catalog_entry.sh docker-entrypoint-dind.sh /  
  
ENTRYPOINT ["/docker-entrypoint-dind.sh"]  
CMD ["java", "-jar", "/bin/swarm-client.jar"]  

