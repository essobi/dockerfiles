FROM ruby:2.2.0  
MAINTAINER Stéphane Cottin <stephane.cottin@vixns.com>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y \  
ca-certificates  
  
RUN gem install --no-rdoc --no-ri riemann-dash thin fog  
  
WORKDIR /app  
  
ADD config.rb /app/  
  
EXPOSE 4567  
CMD [ "riemann-dash" ]  

