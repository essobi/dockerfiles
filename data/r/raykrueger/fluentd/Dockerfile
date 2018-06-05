FROM fluent/fluentd  
  
USER root  
RUN apk --no-cache --update add \  
build-base \  
ruby-dev  
  
#USER fluent  
#RUN gem install fluent-plugin-elasticsearch && \  
# gem install fluent-plugin-mongo  
  
COPY /filesystem/ /  

