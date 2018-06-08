FROM library/ruby:2.3  
MAINTAINER Philipp Daniels <philipp.daniels@gmail.com>  
  
ENV PORTUS_VERSION=2.1.1 \  
PORTUS_PATH=/portus \  
PORTUS_CONFIG_PATH=/portus/config \  
RACK_ENV=production \  
RAILS_ENV=production \  
BUNDLE_GEMFILE=/portus/Gemfile  
  
WORKDIR ${PORTUS_PATH}  
  
# RUNTIME DEPENDENCIES  
RUN set -ex && \  
apt-get update && \  
apt-get install -y --no-install-recommends nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
COPY *.sh ${PORTUS_PATH}/bin/  
  
RUN bin/install.sh  
  
COPY *.yml puma.rb ${PORTUS_CONFIG_PATH}/  
  
CMD exec bin/run.sh  

