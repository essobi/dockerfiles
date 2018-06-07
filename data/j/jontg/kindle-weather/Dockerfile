# FROM hypriot/rpi-ruby  
FROM ruby:2  
RUN apt-get update -y && apt-get install -y librsvg2-bin pngcrush  
  
RUN echo America/Los_Angeles | tee /etc/timezone && dpkg-reconfigure
--frontend noninteractive tzdata  
  
ENV CONFIG_ROOT "/source/config"  
VOLUME [ "/config", "/output" ]  
  
WORKDIR /tmp  
ADD Gemfile /tmp/Gemfile  
ADD Gemfile.lock /tmp/Gemfile.lock  
  
# RUN apt-get install -y --no-install-recommends build-essential libxml2-dev
libxslt-dev && \  
# bundle install --without test development && \  
# apt-get purge -y --auto-remove build-essential && rm -rf
/var/lib/apt/lists/*  
RUN bundle install --without test development  
  
ADD . /source  
WORKDIR /source  
  
CMD ["./weather-script.sh"]  

