FROM fluent/fluentd:latest  
  
MAINTAINER Miroslav Spousta <qiq@ucw.cz>  
  
WORKDIR /home/fluent  
  
COPY fluentd.conf /fluentd/etc/fluentd.conf  
COPY plugins/* /fluentd/plugins/  
  
ENV PATH /home/fluent/.gem/ruby/2.2.0/bin:$PATH  
  
RUN gem install gelf  
  
ENV GRAYLOG2_PROTO=tcp  
ENV GRAYLOG2_HOST=127.0.0.1  
ENV GRAYLOG2_PORT=12201  
ENV FLUENTD_CONF=fluentd.conf  
EXPOSE 24284  
CMD fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT  

