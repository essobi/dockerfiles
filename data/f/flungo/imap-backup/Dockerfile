FROM ruby:alpine  
  
# Install imap-backup  
RUN gem install 'imap-backup'  
  
# Make the data directory a volume  
VOLUME ["/root/.imap-backup"]  
  
# Add and set the entrypoint  
COPY entrypoint.sh /opt/bin/entrypoint.sh  
ENTRYPOINT ["/opt/bin/entrypoint.sh"]  

