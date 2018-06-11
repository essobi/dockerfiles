FROM starefossen/ruby-node:latest  
  
COPY rootfs /  
RUN apt-get -qq -y update  
RUN apt-get -qq -y install \  
g++ make \  
# PostgreSQL dependencies  
libpq-dev \  
# Nokogiri dependencies  
libxml2-dev libxslt-dev \  
# Cypress dependencies  
xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2  
RUN gem install bundler  
RUN gem install rubocop  

