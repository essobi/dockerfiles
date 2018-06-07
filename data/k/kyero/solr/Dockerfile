FROM ruby:2.2.4  
LABEL maintainer "Michael Baudino <michael.baudino@alpine-lab.com>"  
  
# Explicitely define locale  
# as advised in https://github.com/docker-
library/docs/blob/master/ruby/content.md#encoding  
ENV LANG="C.UTF-8"  
# Install apt based dependencies  
RUN sed -i 's/^deb-src/# deb-src/' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
build-essential \  
openjdk-7-jre-headless \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install sunspot_solr -v 2.1.1  
  
# Configure the main working directory.  
RUN mkdir -p /solr/data  
WORKDIR /solr  
  
# Setup Solr  
RUN sunspot-installer /solr  
COPY conf/* /solr/conf/  
  
# Expose port 8982 to the Docker host, so we can access it  
# from the outside.  
EXPOSE 8982  
# The main command to run when the container starts. Also  
# tell the Rails dev server to bind to all interfaces by  
# default.  
CMD ["sunspot-solr", "run", "-s", "/solr", "-d", "/solr/data"]  

