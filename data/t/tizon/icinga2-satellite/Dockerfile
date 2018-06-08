# A docker image for an icinga2 satellite in a docker image  
# https://github.com/TiZon/docker-icinga2-satellite  
  
FROM debian:stretch  
  
LABEL MAINTAINER "Bart De Vos"  
  
ENV ICINGA2_USER_FULLNAME="Icinga2" \  
DOCKER_FQDN="my.docker.machine.domain.tld" \  
ICINGA_MASTER="my.icinga.master.domain.tld" \  
ICINGA_MASTER_PORT="5665" \  
ICINGA_MASTER_TICKET="111111222233334445556677788999"  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
gnupg \  
lsb-release \  
mailutils \  
procps \  
pwgen \  
snmp \  
ssmtp \  
sudo \  
supervisor \  
unzip \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& wget --quiet -O - https://packages.icinga.org/icinga.key \  
| apt-key add - \  
&& echo "deb http://packages.icinga.org/debian icinga-$(lsb_release -cs) main"
> /etc/apt/sources.list.d/icinga2.list \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
icinga2 \  
icingacli \  
monitoring-plugins \  
nagios-nrpe-plugin \  
nagios-snmp-plugins \  
nagios-plugins-contrib \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD content/ /  
  
# Final fixes  
RUN sed -i 's/vars\.os.*/vars.os = "Docker"/' /etc/icinga2/conf.d/hosts.conf \  
&& mv /etc/icinga2/ /etc/icinga2.dist \  
&& mkdir /etc/icinga2 \  
&& usermod -aG nagios www-data \  
&& chmod u+s,g+s \  
/bin/ping \  
/bin/ping6 \  
/usr/lib/nagios/plugins/check_icmp  
  
EXPOSE 5665  
  
# Initialize and run Supervisor  
ENTRYPOINT ["/opt/run"]  

