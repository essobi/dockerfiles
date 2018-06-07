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
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install mailcatcher  
  
# Expose port 1025 for SMTP and 1080 for HTTP (web interface)  
EXPOSE 1025 1080  
# Start MailCatcher  
CMD ["mailcatcher", "--foreground", "--ip=0.0.0.0"]  

