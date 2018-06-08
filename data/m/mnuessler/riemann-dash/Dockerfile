FROM ruby:2.5-slim  
  
MAINTAINER Matthias Nüßler <m.nuessler@web.de>  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install --no-install-recommends build-essential && \  
gem install --no-ri --no-rdoc \  
riemann-dash \  
thin && \  
apt-get -y remove build-essential && \  
apt-get -y autoremove && \  
apt-get clean  
  
EXPOSE 4567  
  
ENTRYPOINT ["riemann-dash"]  

