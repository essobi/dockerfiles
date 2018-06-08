FROM ruby:1.9.3  
MAINTAINER pomu0326@gmail.com  
  
ENV DATA_DIR /opt/data  
  
RUN apt-get update \  
&& apt-get install -y mysql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/pomu0326/webistrano.git /opt/webistrano  
  
WORKDIR /opt/webistrano  
RUN bundle install --path vendor/bundler --without test  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["app:start"]  
  
EXPOSE 3000  
VOLUME ["/opt/data"]  

