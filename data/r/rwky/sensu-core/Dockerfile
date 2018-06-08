FROM ubuntu:16.04  
MAINTAINER Rowan Wookey <admin@rwky.net>  
RUN apt update && apt -y install apt-transport-https && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
EB9C94BB && \  
echo "deb https://sensu.global.ssl.fastly.net/apt xenial main" >
/etc/apt/sources.list.d/sensu.list && \  
apt-get -q update && apt-get -yq install tzdata sensu build-essential
libsasl2-dev curl wget udns-utils && apt-get clean && \  
for p in cpu-checks disk-checks docker filesystem-checks http load-checks
mailer memory-checks network-checks process-checks ssl; do
/opt/sensu/embedded/bin/gem install -N sensu-plugins-$p; done  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
VOLUME /etc/sensu  
ENV PATH=/opt/sensu/bin:/opt/sensu/embedded/bin/:$PATH  
CMD ["sensu-client", "-d", "/etc/sensu/conf.d"]  

