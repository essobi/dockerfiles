# NAME: keyboardstaff/homeland  
FROM homeland/base:0.2.3  
ENV RAILS_ENV 'production'  
RUN curl https://get.acme.sh | sh  
  
RUN useradd ruby -s /bin/bash -m -U &&\  
mkdir -p /var/www &&\  
cd /var/www &&\  
git clone https://github.com/keyboardstaff/homeland.git --depth 1  
RUN cd /var/www/homeland && bundle install --deployment &&\  
find /var/www/homeland/vendor/bundle -name tmp -type d -exec rm -rf {} + &&\  
chown -R ruby:ruby /var/www  
  
WORKDIR /var/www/homeland  

