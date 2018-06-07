FROM debian:squeeze  
MAINTAINER Victor Ladochkin (victor.ladochkin@onlite.net)  
  
ENV NEW_RELIC_LICENSE_KEY YOUR_LICENSE_KEY  
  
# apt-get update  
RUN apt-get update -qq && apt-get install -yq ca-certificates wget  
  
# install new relic server monitoring  
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list  
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN apt-get update  
RUN apt-get install -y -qq newrelic-sysmond  
  
# supervisor  
RUN apt-get install -y -qq supervisor  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
RUN mkdir -p /etc/supervisor/conf.d/  
RUN mkdir -p /var/log/supervisor/  
  
# supervisor-newrelic  
ADD supervisord-newrelic.conf /etc/supervisor/conf.d/newrelic.conf  
  
# enabled supervisord  
CMD nrsysmond-config --set license_key=$NEW_RELIC_LICENSE_KEY && supervisord
-n  

