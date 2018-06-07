FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
ruby-dev \  
gcc \  
make \  
ruby \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install fpm --no-ri --no-rdoc  
  
VOLUME [ "/tmp/fpm" ]  
WORKDIR /tmp/fpm  
  
ENTRYPOINT [ "/usr/local/bin/fpm" ]  
CMD [ "--help" ]

