FROM f21global/java:8  
MAINTAINER Francis Chuang <francis.chuang@boostport.com>  
  
ENV HDP_VER 2.4.2.0  
RUN apt-get update \  
&& apt-get install -y ca-certificates xmlstarlet wget \  
&& wget http://public-
repo-1.hortonworks.com/HDP/ubuntu14/2.x/updates/$HDP_VER/hdp.list -O
/etc/apt/sources.list.d/hdp.list \  
&& gpg --keyserver pgp.mit.edu --recv-keys B9733A7A07513CAD \  
&& gpg -a --export 07513CAD | apt-key add - \  
&& apt-get update  
  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$arch" \  
&& chmod +x /usr/local/bin/gosu

