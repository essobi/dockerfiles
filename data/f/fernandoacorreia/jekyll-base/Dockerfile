FROM debian:wheezy  
MAINTAINER Fernando de Alcântara Correia <fernando@fernandocorreia.info>  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
curl \  
ruby \  
ruby-dev \  
&& curl -sL https://deb.nodesource.com/setup | bash - \  
&& apt-get install -y nodejs \  
&& gem install --no-ri \--no-rdoc \  
jekyll \  
&& mkdir /src \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y \  
build-essential \  
ruby-dev \  
&& DEBIAN_FRONTEND=noninteractive apt-get autoremove -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get clean \  
&& rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4000  
VOLUME /src  
WORKDIR /src  
ENTRYPOINT ["jekyll"]  

