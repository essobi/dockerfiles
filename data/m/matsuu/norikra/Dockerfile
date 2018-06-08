FROM jruby:9-alpine  
  
RUN gem install norikra --no-ri --no-rdoc  
  
EXPOSE 26571 26578  
VOLUME /var/norikra  
  
ENTRYPOINT ["norikra", "start"]  
CMD ["--stats=/var/norikra/stats.json", "--dump-stat-interval=60"]  

