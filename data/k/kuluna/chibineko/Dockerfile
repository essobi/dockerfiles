FROM ruby:2.3.0  
MAINTAINER kuluna  
  
# Download chibineko  
RUN git clone https://github.com/tabbyz/chibineko.git /opt/chibineko  
  
# Setup  
WORKDIR /opt/chibineko  
RUN mv config/mailer.yml.example config/mailer.yml  
RUN bundle install  
RUN rake db:migrate  
RUN rake db:seed  
  
# Port  
EXPOSE 3000  
# Volume  
VOLUME /opt/chibineko/db  
  
# Start server  
CMD rm -f /chibineko/tmp/pids/server.pid;rails server -b 0.0.0.0  

