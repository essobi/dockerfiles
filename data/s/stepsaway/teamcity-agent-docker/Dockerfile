  
FROM stepsaway/baseimage:1.0.1  
MAINTAINER StepsAway <devgru@stepsaway.com>  
  
# VERSIONS  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION 1.11.1  
ENV DOCKER_SHA256
893e3c6e89c0cd2c5f1e51ea41bc2dd97f5e791fcfa3cee28445df277836339d  
ENV RANCHER_COMPOSE v0.8.5  
ENV DOCKER_COMPOSE 1.7.1  
  
ENV PACKAGES python-pip lxc aufs-tools ca-certificates software-properties-
common unzip git ssh heroku-toolbelt  
ENV TERM xterm-256color  
ENV AGENT_DIR /opt/buildAgent  
  
# Install java-8-oracle and key packages  
RUN echo "deb http://toolbelt.heroku.com/ubuntu ./" >
/etc/apt/sources.list.d/heroku.list && \  
curl -s https://toolbelt.heroku.com/apt/release.key | apt-key add - && \  
apt-get update && \  
apt-get install -y --no-install-recommends $PACKAGES && \  
rm -rf /var/lib/apt/lists/* && \  
add-apt-repository -y ppa:webupd8team/java && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && \  
apt-get install -y oracle-java8-installer ca-certificates-java && \  
rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk8-installer/*.tar.gz
/usr/lib/jvm/java-8-oracle/src.zip /usr/lib/jvm/java-8-oracle/javafx-src.zip \  
/usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts && \  
ln -s /etc/ssl/certs/java/cacerts
/usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts && \  
update-ca-certificates && \  
printf "\n--> Installing docker and related tools\n" && \  
set -x && \  
curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
docker.tgz && \  
echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - && \  
tar -xzvf docker.tgz && \  
mv docker/* /usr/local/bin/ && \  
rmdir docker && \  
rm docker.tgz && \  
docker -v && \  
curl -o /usr/local/bin/docker-compose -SL
https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE/docker-
compose-Linux-x86_64 && \  
wget -qO- https://github.com/rancher/rancher-
compose/releases/download/$RANCHER_COMPOSE/rancher-compose-linux-
amd64-$RANCHER_COMPOSE.tar.gz | tar xz -C /tmp && \  
mv /tmp/rancher-compose-$RANCHER_COMPOSE/rancher-compose /usr/local/bin/ && \  
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh && \  
chmod +x -R /usr/local/bin && \  
mkdir -p $AGENT_DIR && \  
pip install --upgrade awscli  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
COPY agent-start.sh /etc/my_init.d/50-agent-start.sh  

