FROM ruby:slim  
  
RUN echo gem: --no-document > /etc/gemrc  
  
RUN gem install systemd_mon  
RUN gem install mail  
RUN gem install slack-notifier  
RUN gem install hipchat  
  
RUN mkdir -p /etc/systemd_mon  
  
RUN echo "---\nverbose: true" > /etc/systemd_mon/config.yml  
  
ENTRYPOINT ["/usr/local/bin/systemd_mon"]  
  
CMD ["/etc/systemd_mon/config.yml"]  

