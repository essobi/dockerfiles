FROM unit9/base:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN curl -fsS https://sensu.global.ssl.fastly.net/apt/pubkey.gpg \  
| apt-key add - \  
&& echo "deb https://sensu.global.ssl.fastly.net/apt jessie main" \  
> /etc/apt/sources.list.d/sensu.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install --yes --no-install-recommends \  
jq \  
monitoring-plugins \  
nagios-plugins-contrib \  
nagios-snmp-plugins \  
sensu \  
&& rm -rf /var/cache/apt /var/lib/apt/lists \  
&& ls -ld /opt/sensu/bin/sensu-*  
  
COPY sensu.env /opt/sensu/sensu.env  
  
RUN /opt/sensu/sensu.env gem install sensu-plugin  
  
COPY rc.local /etc/rc.local  
  
VOLUME /etc/sensu/conf.d/ \  
/etc/sensu/secrets/ \  
/etc/sensu/ssl/  

