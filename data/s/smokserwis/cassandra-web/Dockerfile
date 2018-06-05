FROM library/ruby:2.2  
ENV PORT=9042 \  
HOSTS=127.0.0.1  
RUN gem install cassandra-web  
  
ADD entry.sh /entry.sh  
RUN chmod ugo+x /entry.sh  
ENTRYPOINT /entry.sh  
  
EXPOSE 3000  

