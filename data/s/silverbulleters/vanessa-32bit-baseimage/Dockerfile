FROM daald/ubuntu32:trusty  
MAINTAINER "Shenja Sosna" <shenja@sosna.zp.ua>  
  
RUN nc -z w3 consul-io.node.cloud.consul 3142 && echo 'Acquire::http { Proxy
"http://consul-io.node.cloud.consul:3142"; };' >> /etc/apt/apt.conf.d/01proxy
|| echo "not found"  
RUN echo 'precedence ::ffff:0:0/96 100' >> /etc/gai.conf  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections \  
&& echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >
/etc/apt/sources.list.d/multiverse.list \  
&& apt-get update \  
&& apt-get install -y ca-certificates locales python-pip gcc wget curl
language-pack-ru language-pack-ru-base \  
language-pack-uk language-pack-uk-base software-properties-common \  
imagemagick libfreetype6 libgsf-bin libodbc1 \  
ttf-mscorefonts-installer \  
&& curl -o /usr/local/bin/gosu -fsSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu \  
&& pip install dumb-init \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG ru_RU.UTF-8  
RUN locale-gen ru_RU && locale-gen ru_RU.UTF-8 \  
&& locale-gen uk_UA && locale-gen uk_UA.UTF-8 \  
&& update-locale LANG=ru_RU.UTF-8  
  

