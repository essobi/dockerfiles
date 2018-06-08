FROM ruby:2.5.0-alpine  
MAINTAINER Yuya.Nishida.  
  
RUN set -x && \  
apk add --no-cache --virtual build-dependencies build-base libxml2-dev
libxslt-dev && \  
gem install --no-doc --no-ri nokogiri && \  
apk del build-dependencies && \  
wget -O/usr/local/bin/cssgrep
https://raw.githubusercontent.com/nono/cssgrep/ce02b340ea4fe3fa3131740d920a51e87b0ccbe7/cssgrep.rb
&& \  
chmod a+x /usr/local/bin/cssgrep && \  
apk add --no-cache w3m curl  
  
COPY webupdates /usr/local/bin/  
ENV DATA_PATH=/var/lib/webupdates  
ENTRYPOINT ["/usr/local/bin/webupdates"]  

