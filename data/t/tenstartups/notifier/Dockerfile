#  
# Notifier docker image  
#  
# http://github.com/tenstartups/notifier-docker  
#  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Install base packages.  
RUN \  
apk --update add build-base ruby ruby-dev ruby-json && \  
rm -rf /var/cache/apk/*  
  
# Install ruby gems.  
RUN gem install colorize hipchat rest-client slack-notifier --no-document  
  
# Add files to the container.  
COPY entrypoint.sh /docker-entrypoint  
ADD script /tmp/script  
  
# Copy scripts and configuration into place.  
RUN \  
find /tmp/script -type f -name '*.sh' | while read f; do cp -v "$f"
"/usr/local/bin/`basename ${f%.sh}`"; done && \  
find /tmp/script -type f -name '*.rb' | while read f; do cp -v "$f"
"/usr/local/bin/`basename ${f%.rb}`"; done && \  
rm -rf /tmp/script  
  
# Define entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Define default command.  
CMD ["/usr/local/bin/notify"]  

