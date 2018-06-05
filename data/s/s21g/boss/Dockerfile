FROM ruby:alpine  
  
RUN apk --no-cache add git  
RUN gem install -N specific_install sinatra  
RUN gem specific_install -l https://github.com/a09-capf/docker-api \  
-b remote-api-1.25 -r f452561dec475bd5eddcfcaf9ad03d556127d0a7  
COPY ./boss /usr/bin/boss  
  
ENV DOCKER_URL unix:///var/run/docker.sock  
ENV INTERVAL 300  
ENV RACK_ENV production  
EXPOSE 21081  
ENTRYPOINT ["boss"]  

