FROM shift/ruby:latest  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /  
RUN apt-get update \  
&& apt-get install curl --yes \  
&& curl -L -O https://github.com/sensu/sensu/archive/v0.20.5.tar.gz \  
&& tar xfvz v0.20.5.tar.gz \  
&& mv sensu-0.20.5 sensu \  
&& cd sensu \  
&& sed -i.bak 's/s\.add_dependency "eventmachine", "1\.0\.3"/s\.add_dependency
"eventmachine", "1\.0\.8"/' sensu.gemspec \  
&& bundle install \  
&& gem install sensu-plugins-slack \  
&& gem install sensu-plugins-github \  
&& gem install sensu-plugins-dns \  
&& gem install sensu-plugins-network-checks \  
&& gem install sensu-plugins-docker \  
&& gem install sensu-plugins-redis \  
&& gem install sensu-plugins-influxdb \  
&& gem install sensu-plugins-graphite \  
&& gem install sensu-plugins-rabbitmq \  
&& gem install sensu-plugins-elasticsearch \  
&& gem install sensu-plugins-ssl \  
&& gem install sensu-plugins-ntp \  
&& gem install sensu-plugins-postgres \  
&& gem install sensu-plugins-openvpn \  
&& rm -rf ../v0.20.5.tar.gz \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /etc/sensu  
VOLUME /data  
VOLUME /logs  

