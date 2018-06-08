FROM unit9/sensu-base:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install --yes \--no-install-recommends \  
build-essential \  
&& /opt/sensu/embedded/bin/gem install \  
mail \  
mime-types \  
redphone \  
sensu-plugin \  
sensu-plugins-aws \  
sensu-plugins-mailer \  
sensu-plugins-pagerduty \  
xml-simple \  
&& apt-get remove --yes build-essential \  
&& apt-get autoremove --yes \  
&& rm -rf /var/cache/apt /var/lib/apt/lists \  
&& true  
  
COPY check-sensu-config.sh /etc/rc.local.d/99-check-sensu-config  
COPY sensu-server.run /etc/service/sensu-server/run  
COPY sensu-api.run /etc/service/sensu-api/run  
  
EXPOSE 4567  

