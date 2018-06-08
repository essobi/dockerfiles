# Dockerfile for One-Time Secret http://onetimesecret.com  
FROM debian:stretch  
  
LABEL MAINTAINER ant <git@manchestermonkey.co.uk>  
  
RUN apt-get -qq update && apt-get install -qq ntp build-essential libyaml-dev
libevent-dev unzip zlib1g zlib1g-dev openssl libssl-dev libxml2 ruby ruby-dev
bundler  
  
RUN useradd ots -d /var/lib/onetime && mkdir /var/lib/onetime && chown ots:
/var/lib/onetime  
  
ADD https://github.com/onetimesecret/onetimesecret/archive/master.zip
/tmp/onetime.zip  
  
RUN /usr/bin/unzip /tmp/onetime.zip -d /var/lib/onetime/ && /bin/mv
/var/lib/onetime/onetimesecret-master/* /var/lib/onetime/  
  
WORKDIR /var/lib/onetime  
  
RUN bundle install --frozen --deployment --without=dev && \  
bin/ots init && \  
mkdir -p /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime &&
chown ots /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime && \  
cp -R etc/* /etc/onetime/ && chown ots: /var/lib/onetime/* -R  
  
ADD config/config /etc/onetime/config  
ADD config/fortunes /etc/onetime/fortunes  
  
EXPOSE 7143  
  
ENTRYPOINT su -c 'bundle exec thin -e dev -R config.ru -p 7143 start' ots  

