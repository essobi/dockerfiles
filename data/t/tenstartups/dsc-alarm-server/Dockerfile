#  
# DSC Alarm Server  
#  
# http://github.com/tenstartups/dsc-alarm-server  
#  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment variables.  
ENV \  
PAGER=more \  
RUBYLIB=/usr/local/lib/ruby  
  
# Install packages.  
RUN \  
apk --update add \  
build-base \  
git \  
libxml2-dev \  
libxslt-dev \  
ruby \  
ruby-bigdecimal \  
ruby-bundler \  
ruby-dev \  
ruby-irb \  
ruby-io-console \  
ruby-json \  
zlib-dev && \  
rm -rf /var/cache/apk/*  
  
# Install unf_ext gem from source  
RUN \  
cd /tmp && \  
git clone https://github.com/knu/ruby-unf_ext.git && \  
cd ruby-unf_ext && \  
gem build unf_ext.gemspec && \  
gem install unf_ext --no-document && \  
gem install unf_ext --local \--ignore-dependencies --no-document && \  
cd .. && \  
rm -rf ruby-unf_ext  
  
# Install gems.  
RUN \  
gem install --no-document \  
activesupport \  
awesome_print \  
colorize \  
nokogiri \  
pry \  
puma \  
recursive-open-struct \  
rest-client \  
sinatra \  
slack-notifier \  
ssdp \  
tzinfo-data  
  
# Add files to the container.  
COPY lib ${RUBYLIB}  
COPY entrypoint.rb /docker-entrypoint  
  
# Set the entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Set the default command.  
CMD ["server"]  

