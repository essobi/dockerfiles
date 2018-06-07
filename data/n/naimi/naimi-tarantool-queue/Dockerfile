FROM ubuntu:xenial  
  
MAINTAINER Amangeldy Kadyl <lex0.kz@gmail.com>  
  
RUN apt-get update && \  
apt-get install curl lsb-release -y && \  
curl http://download.tarantool.org/tarantool/1.7/gpgkey | apt-key add - && \  
release=`lsb_release -c -s` && \  
apt-get -y install apt-transport-https && \  
echo "deb http://download.tarantool.org/tarantool/1.7/ubuntu/ ${release} main"
> \  
/etc/apt/sources.list.d/tarantool_1_7.list && \  
echo "deb-src http://download.tarantool.org/tarantool/1.7/ubuntu/ ${release}
main" >> \  
/etc/apt/sources.list.d/tarantool_1_7.list && \  
apt-get update && \  
curl -o /bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.9/gosu-$(dpkg --print-
architecture)" && \  
chmod +x /bin/gosu && \  
apt-get -y install tarantool tarantool-queue  
  
VOLUME /var/lib/tarantool  
  
COPY run.sh /run.sh  
COPY queue.lua /etc/tarantool/instances.enabled/queue.lua  
  
EXPOSE 3301  
CMD ["/run.sh"]  

