FROM ubuntu:14.04  
# Derived from jplock/rsyslog  
# Credit to original maintainer Justin Plock <justin@plock.net>  
# Derived from panoptix / rsyslog  
# Credit to original maintainer Stephan Buys <stephan.buys@panoptix.co.za>  
# Using papertrail and TLS  
MAINTAINER Konstantinos Servis <kostas@everydayhero.com.au>  
  
ENV REFRESHED_ON "10 Nov 2014"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y -q install software-properties-common  
RUN apt-get update && apt-get -y -q install python-software-properties  
RUN add-apt-repository ppa:adiscon/v8-stable  
RUN apt-get update && apt-get -y -q install rsyslog  
RUN apt-get update && apt-get -y -q install bundler  
RUN apt-get update && apt-get -y -q install curl  
  
ADD rsyslog.conf.erb /root/  
ADD paperweight.conf.erb /root/  
ADD loggly.conf.erb /root/  
ADD set_etcd_from_env.rb /root/  
ADD template_from_etcd.rb /root/  
ADD Gemfile /root/  
ADD Gemfile.lock /root/  
ADD start_rsyslog.sh /root/  
ADD papertrail-bundle.pem.md5 /etc/  
  
RUN cd /etc/ && curl -O https://papertrailapp.com/tools/papertrail-bundle.pem  
RUN cd /etc/ && md5sum -c papertrail-bundle.pem.md5  
  
RUN cd /root && bundle install  
  
# Make sure that these ports are the same that deis expects  
EXPOSE 514/tcp 514/udp  
  
CMD ["/root/start_rsyslog.sh"]  

