#  
# Slack webhook command runner for home automation scripts  
#  
# http://github.com/tenstartups/slack-ha-controller-docker  
#  
FROM tenstartups/alpine:latest  
  
MAINTAINER Marc Lennox <marc.lennox@gmail.com>  
  
# Set environment variables.  
ENV \  
RUBYLIB=/usr/local/lib/ruby  
  
# Install packages.  
RUN \  
apk --update add \  
build-base libxml2-dev libxslt-dev ruby ruby-bigdecimal ruby-bundler ruby-dev
\  
ruby-irb ruby-io-console ruby-json zlib-dev && \  
rm -rf /var/cache/apk/*  
  
# Install gems.  
RUN \  
gem install \  
activesupport awesome_print colorize nokogiri pry puma \  
recursive-open-struct rest-client sinatra slack-notifier tzinfo-data \  
\--no-document  
  
# Add files to the container.  
COPY entrypoint.rb /docker-entrypoint  
ADD lib ${RUBYLIB}  
  
# Define entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Expose default ports  
EXPOSE 8080  
# Default command  
CMD ["server"]  

