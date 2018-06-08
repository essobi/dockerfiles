FROM ruby:2-alpine  
RUN gem install capistrano:3.4.0  
RUN gem install highline  
RUN mkdir /app  
VOLUME /app  
WORKDIR /app  
COPY cap-wrap.sh /cap-wrap.sh  
RUN chmod +x /cap-wrap.sh  
ENTRYPOINT ["/cap-wrap.sh"]

