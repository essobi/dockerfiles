FROM wenzizone/base-upstart  
MAINTAINER wenzizone <wenzizone@126.com>  
  
##### sensu-server part #####  
RUN apt-get update && apt-get install -y wget ca-certificates && apt-get -y
clean && rm -rf /var/lib/apt/lists/*  
RUN wget -q http://repositories.sensuapp.org/apt/pubkey.gpg -O- | sudo apt-key
add -  
RUN echo "deb http://repositories.sensuapp.org/apt sensu main" | sudo tee
/etc/apt/sources.list.d/sensu.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install sensu && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD config/sensu_config.json /etc/sensu/config.json  
  
ADD init/sensu-server.conf /etc/init/sensu-server.conf  
ADD init/sensu-api.conf /etc/init/sensu-api.conf  
#ADD init/sensu-client.conf /etc/init/sensu-client.conf  
ADD config/extension/influxdb.rb /etc/sensu/extensions/influxdb.rb  
ADD config/handlers/metrics.json /etc/sensu/conf.d/handlers/metrics.json  
ADD config/influxdb.json /etc/sensu/conf.d/influxdb.json  
  
##### uchiwa part #####  
# gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
ruby \  
ruby-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV UCHIWA_VERSION 0.13.0-1  
RUN set -x; \  
wget http://dl.bintray.com/palourde/uchiwa/uchiwa_${UCHIWA_VERSION}_amd64.deb
-O uchiwa.deb \  
&& ls -l uchiwa.deb \  
&& dpkg --force-depends -i uchiwa.deb \  
&& apt-get update \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* uchiwa.deb  
  
RUN mkdir /var/log/uchiwa  
ADD init/uchiwa.conf /etc/init/uchiwa.conf  
ADD config/uchiwa.json /etc/sensu/uchiwa.json  
  
###### install sensu-plugin #######  
RUN echo 'EMBEDDED_RUBY=false' > /etc/default/sensu  
RUN sensu-install -P cpu-checks,disk-checks,process-checks,memory-
checks,http,uptime-checks,load-checks,docker,network-checks,io-checks  
  
EXPOSE 3000

