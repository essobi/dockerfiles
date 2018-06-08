FROM ruby:2.2.1-onbuild  
ENTRYPOINT ["bundle", "exec"]  
ENV INFLUXDB_DATABASE=test  
ENV INFLUXDB_HOST=localhost  
ENV INFLUXDB_PORT=8086  
ENV INFLUXDB_USERNAME=elb-stats  
ENV INFLUXDB_PASSWORD=password  
ENV INFLUXDB_SSL=false  
ENV ELB_NAMES=default  
CMD ["ruby", "elb-stats.rb"]  

