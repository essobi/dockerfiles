FROM node:4.4  
MAINTAINER Andras Simon <andras@cabsolutely.co>  
  
  
ENV STATSD_VERSION 0.8.0  
RUN rm -rf /opt/statsd  
RUN git clone -b v0.8.0 https://github.com/etsy/statsd.git /opt/statsd  
RUN cd /opt/statsd && npm install git+https://github.com/gillesdemey/statsd-
influxdb-backend.git  
  
# Configure StatsD  
COPY ./config.js /opt/statsd/config.js.tmpl  
COPY ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

