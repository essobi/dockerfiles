FROM danieldent/elixir-lang:1.2.0  
MAINTAINER Daniel Dent (https://www.danieldent.com)  
  
ADD https://deb.nodesource.com/gpgkey/nodesource.gpg.key
/tmp/nodesource.gpg.key  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install apt-transport-https \  
&& echo "773b328f7b1d6db58a8c6a7fc89e2ed58ac5e06c3ab148411cf8272be7b1c472
/tmp/nodesource.gpg.key" | sha256sum -c \  
&& apt-key add /tmp/nodesource.gpg.key \  
&& echo 'deb https://deb.nodesource.com/node_4.x trusty main' >
/etc/apt/sources.list.d/nodesource.list \  
&& DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install git inotify-tools
nodejs=4.4.0-1nodesource1~trusty1 postgresql-client \  
&& rm -rf /var/lib/apt/* /var/cache/apt/* \  

