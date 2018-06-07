FROM jenkins:2.19.1  
  
USER root  
RUN apt-get update \  
&& apt-get install -y apt-utils \  
&& apt-get install -y apt-transport-https ca-certificates \  
&& apt-key adv \--keyserver hkp://p80.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D  
  
COPY docker.list /etc/apt/sources.list.d/docker.list  
  
RUN apt-get update \  
&& apt-get install -y \  
docker-engine git build-essential subversion libncurses5-dev zlib1g-dev \  
unzip ccache gawk wget libssl-dev libxml-parser-perl file rsync groff-base  
  
USER jenkins  

