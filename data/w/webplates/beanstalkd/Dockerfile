FROM debian:jessie  
  
RUN set -x \  
&& addgroup --system beanstalk \  
&& adduser --disabled-password --disabled-login --system --ingroup beanstalk
beanstalk  
  
RUN set -xe \  
&& buildDeps=" \  
gcc \  
libtool \  
make \  
" \  
&& apt-get update && apt-get install -y $buildDeps ca-certificates curl tar
--no-install-recommends && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& curl -fSL "https://github.com/kr/beanstalkd/archive/v1.10.tar.gz" -o
beanstalk.tar.gz \  
&& mkdir /usr/src/beanstalk \  
&& tar -xzf /usr/src/beanstalk.tar.gz -C "/usr/src/beanstalk" \--strip-
components=1 \  
&& cd /usr/src/beanstalk \  
&& make \  
&& cp beanstalkd /usr/bin/beanstalkd \  
&& cd \  
&& rm -r /usr/src/beanstalk \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  
COPY entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 11300  
CMD ["beanstalkd"]

