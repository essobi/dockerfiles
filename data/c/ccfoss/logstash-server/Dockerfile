FROM ccfoss/alpine-consul  
MAINTAINER Chaitanya Akkineni cakkinen@cisco.com  
  
ENV LOGSTASH_VERSION 5.1.1  
  
RUN apk add --update bash libzmq openjdk8-jre gosu@testing && \  
rm -rf /var/cache/apk/*  
  
RUN apk add --update wget ca-certificates &&\  
cd /tmp &&\  
wget -O logstash.tar.gz
https://artifacts.elastic.co/downloads/logstash/logstash-$LOGSTASH_VERSION.tar.gz
&&\  
tar -xzf logstash.tar.gz &&\  
mv logstash-$LOGSTASH_VERSION /usr/local/logstash &&\  
mkdir -p /etc/logstash/conf.d &&\  
adduser -DH -s /sbin/nologin logstash &&\  
chown -R logstash:logstash /usr/local/logstash &&\  
chown -R logstash:logstash /etc/logstash &&\  
ln -s /usr/local/logstash/bin/logstash /usr/local/bin/logstash &&\  
rm -rf /tmp/* &&\  
rm -rf /var/cache/apk/*  
  
ENV PATH /usr/share/logstash/bin:/sbin:$PATH  
ENV LS_SETTINGS_DIR /etc/logstash  
  
EXPOSE 5601  
  
ADD logstash.yml.ctmpl /tmp/  
ADD consul-template.hcl /etc/consul.d/  
ADD logstash.yml /etc/logstash  
CMD ["logstash", "-f", "/etc/logstash/conf.d"]  

