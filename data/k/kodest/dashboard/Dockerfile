FROM ruby:2.5  
RUN true \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends nodejs \  
&& gem install smashing \  
&& smashing new dash1 \  
&& cd dash1 \  
&& bundle  
  
WORKDIR /dash1  
EXPOSE 3030  
ENTRYPOINT ["smashing", "start"]  

