FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get dist-upgrade --yes \  
&& apt-get install --no-install-recommends --yes wget ca-certificates \  
&& wget -O - http://repositories.sensuapp.org/apt/pubkey.gpg | apt-key add - \  
&& echo "deb http://repositories.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list \  
&& apt-get --yes clean \  
&& rm -rf /var/lib/apt/lists  
  
ENV DUMB_INIT_VERSION 1.2.0  
RUN wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64.deb \  
&& dpkg -i dumb-init_${DUMB_INIT_VERSION}_amd64.deb \  
&& rm dumb-init_${DUMB_INIT_VERSION}_amd64.deb  
  
ENV SENSU_VERSION 0.26.5-2  
RUN apt-get update \  
&& apt-get install sensu=$SENSU_VERSION \  
&& apt-get --yes clean \  
&& rm -rf /var/lib/apt/lists  
  
RUN apt-get update \  
&& apt-get install --yes --no-install-recommends \  
g++ \  
make \  
ruby-dev \  
libmysqlclient-dev \  
  
&& /opt/sensu/embedded/bin/gem install --no-document \  
  
sensu-plugins-graphite:2.0.0 \  
sensu-plugins-logstash:0.1.0 \  
sensu-plugins-hipchat:0.0.4 \  
  
&& apt-get autoremove --yes --purge ruby-dev g++ make \  
&& apt-get --yes clean \  
&& rm -rf /var/lib/apt/lists  
  
  
RUN rm -rf /etc/sensu/*  
VOLUME ["/etc/sensu"]  
  
ADD sensu /sensu  
  
USER sensu  
  
ENTRYPOINT ["/sensu"]  

