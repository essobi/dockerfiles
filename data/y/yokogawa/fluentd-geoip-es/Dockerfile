FROM ruby:2.2  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libgeoip-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
COPY Gemfile /opt/fluentd/  
RUN cd /opt/fluentd \  
&& bundle install  
WORKDIR /opt/geoip  
RUN curl -LO
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \  
&& gzip -vd GeoLiteCity.dat.gz  
  
WORKDIR /work  
ENTRYPOINT ["fluentd"]  
CMD ["--help"]  
  

