FROM ruby:2.3  
RUN apt-get update -qq && \  
apt-get install -y libldap2-dev libsasl2-dev && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
WORKDIR /opt  
  
VOLUME ["/opt/geminabox-data"]  
  
COPY Gemfile .  
RUN bundle install  
  
COPY config.ru .  
COPY config.yml .  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["rackup", "-o", "0.0.0.0", "-p", "80"]

