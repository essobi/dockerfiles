FROM fluent/fluentd:v0.12.29-onbuild  
MAINTAINER Jarrold Ong  
  
USER fluent  
  
COPY fluent.conf /fluentd/etc/  
  
WORKDIR /home/fluent  
ENV PATH /home/fluent/.gem/ruby/2.2.0/bin:$PATH  
RUN gem install fluent-plugin-secure-forward  
RUN gem install fluent-plugin-parser  
RUN gem install fluent-plugin-elasticsearch  
RUN gem install fluent-plugin-slack  
RUN gem install fluent-plugin-grep  
  
EXPOSE 24284  
CMD fluentd -c /fluentd/etc/fluent.conf -p /fluentd/plugins $FLUENTD_OPT  

