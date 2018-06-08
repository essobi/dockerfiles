################################################################################  
# Base image  
################################################################################  
  
FROM docker:17.05.0-ce-dind  
MAINTAINER Billy Nguyen <billy.nguyen@noria.no>  
  
################################################################################  
# Build instructions  
################################################################################  
ENV SWARM_CLIENT_VERSION=3.6 \  
DOCKER_COMPOSE_VERSION=1.11.2 \  
DOCKER_EXTRA_OPTS="" \  
COMMAND_OPTIONS="" \  
JMETER_VERSON="3.3"  
  
ENV JMETER_HOME=/root/apache-jmeter-$JMETER_VERSON  
ENV PATH=$JMETER_HOME/bin:$PATH  
  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
RUN set -ex; \  
addgroup -S jenkins; \  
addgroup -S docker; \  
adduser -D -S H -s /sbin/nologin -G jenkins -G dockremap -G docker jenkins; \  
echo "http://php.codecasts.rocks/v3.5/php-7.1" >> /etc/apk/repositories; \  
apk add --update --no-cache --virtual .run-deps \  
bash \  
rsync \  
openjdk8-jre \  
openssh-client \  
sshpass \  
git \  
wget \  
curl \  
zip \  
php7 \  
php7-common \  
php7-ctype \  
php7-mbstring \  
php7-json \  
php7-bcmath \  
php7-curl \  
php7-sockets \  
php7-mysqlnd \  
php7-pdo \  
php7-pdo_mysql \  
python \  
; \  
  
# Install docker-compose, supervisor  
curl https://bootstrap.pypa.io/get-pip.py -o - | python; \  
pip install docker-compose supervisor supervisor-stdout; \  
  
# Install Jenkins Swarm Client  
wget -q https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}.jar -P
/root; \  
  
#Install Jmeter  
  
wget -O - http://www-us.apache.org/dist//jmeter/binaries/apache-
jmeter-${JMETER_VERSON}.tgz --progress=bar --tries=3 | tar xzf - -C /root  
  
ADD supervisord.conf /etc/supervisord.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord"]

