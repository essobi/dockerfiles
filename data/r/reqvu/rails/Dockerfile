FROM reqvu/ruby  
  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
ENV RAILS_VERSION 4.2.6  
  
RUN gem install rails --version "$RAILS_VERSION"  
  
CMD [ "bash" ]

