FROM ruby:2.4-alpine  
  
RUN apk update && apk add bind-tools curl ca-certificates build-base \  
&& addgroup -S -g 7777 pry \  
&& adduser -s /bin/sh -u 7777 -G pry -D pry \  
&& cd /home/pry \  
&& su pry -c 'gem install pry faraday hal-client' \  
&& apk del build-base \  
&& su pry -c 'printf "%s\n" "Pry.pager = false" > .pryrc' \  
&& su pry -c 'mkdir work'  
WORKDIR /home/pry/work  
USER pry  
  
ENTRYPOINT [ "env", "pry", "-r", "faraday", "-r", "hal-client", "-r", "json",
"-r", "yaml" ]  

