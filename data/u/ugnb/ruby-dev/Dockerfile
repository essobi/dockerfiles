FROM phusion/baseimage  
  
RUN /usr/sbin/enable_insecure_key  
RUN rm -f /etc/service/sshd/down  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y git-core curl zlib1g-dev build-essential libssl-
dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
libxslt1-dev libcurl4-openssl-dev python-software-properties libpq-dev  
RUN sudo apt-get install -y wget  
RUN mkdir /tmp/ruby-dist  
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz -O /tmp/ruby-
dist.tar.gz  
RUN tar -xzf /tmp/ruby-dist.tar.gz -C /tmp/ruby-dist --strip-components=1  
RUN cd /tmp/ruby-dist  
RUN /tmp/ruby-dist/configure  
RUN make && make install  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
  
RUN gem install bundler  
  
RUN sudo apt-get install -y nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN sudo apt-get install -y npm  
RUN npm install -g bower  
  
ENV RAILS_ENV development  
ENV RAILS_SERVE_STATIC_FILES true  
ENV RAILS_SECRET_KEY_BASE =$(openssl rand -base64 32)  
  
VOLUME /workspace  
  
EXPOSE 80  
EXPOSE 22  
CMD ["/sbin/my_init"]  

