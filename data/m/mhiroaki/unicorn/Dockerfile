FROM ruby:alpine  
  
RUN apk -U add gcc make libc-dev linux-headers \  
&& gem install unicorn rack\  
&& addgroup -S unicorn \  
&& adduser -h /unicorn -s /bin/false -S -D -H -G unicorn unicorn \  
&& install -d /var/log/unicorn -o unicorn -g unicorn \  
&& ln -s /dev/stdout /var/log/unicorn/stdout.log \  
&& ln -s /dev/stderr /var/log/unicorn/stderr.log  
  
ADD unicorn.rb /etc/unicorn.rb  
ADD config.ru /unicorn/config.ru  
  
USER unicorn  
WORKDIR /unicorn  
EXPOSE 8000  
ENTRYPOINT [ "unicorn" ]  
CMD [ "-c", "/etc/unicorn.rb"]  

