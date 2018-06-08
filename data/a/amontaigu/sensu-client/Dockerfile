#
================================================================================================================  
#  
# Sensu server customized to act as a client and with docker options.  
#  
# @see https://github.com/AlbanMontaigu/docker-sensu-server  
# @see https://github.com/hiroakis/docker-sensu-server  
# @see https://github.com/usmanismail/docker-sensu-client  
# @see http://rancher.com/comparing-monitoring-options-for-docker-deployments/  
#
================================================================================================================  
# Base image  
FROM amontaigu/sensu-server  
  
# Maintainer  
MAINTAINER alban.montaigu@gmail.com  
  
# Environment configuration  
ENV DOCKER_VERSION="1.12.2"  
# System install required system components  
RUN apt-get update \  
&& apt-get -y install netcat-openbsd curl \  
&& rm -r /var/lib/apt/lists/* \  
  
# Install docker bin for client commands (will be connected to docker host
daemon)  
&& curl -fSL
"https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& tar xvzf docker.tgz \  
&& mv -fv docker/docker /usr/local/bin/docker \  
&& chmod +x /usr/local/bin/docker \  
&& rm -rvf docker*  
  
# Supervisor configuration  
ADD ./supervisor/supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Sensu configuration  
ADD ./sensu/config.json /tmp/sensu/config.json  
ADD ./sensu/client.json /tmp/sensu/conf.d/client.json  
  
# Sensu need to be root to execute docker commands  
RUN sed -i -e "s%USER=sensu%USER=root%g" /etc/init.d/sensu-service  
  
# Entrypoint setting  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

