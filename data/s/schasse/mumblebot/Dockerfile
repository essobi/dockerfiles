FROM ruby:2.3  
RUN \  
apt-get update && \  
apt-get install -y mpd mpc libopus-dev  
RUN apt-get clean  
COPY mpd.conf /etc/  
RUN mkdir -p /run/mpd  
RUN mkdir -p /var/lib/mpd  
RUN mkdir -p /var/lib/mpd/tmp  
  
COPY Gemfile .  
COPY Gemfile.lock .  
RUN bundle  
COPY mumblebot.rb .  
  
CMD ./mumblebot.rb  

