FROM inspiredgeek/redmine-alpine:3.4  
  
LABEL maintainer="Alexey Ivanov <lexa.ivanov@gmail.com>" \  
org.label-schema.docker.dockerfile="./3.4/unicorn/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="redmine-alpine" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/inspired-geek/redmine-alpine" \  
org.label-schema.version="3.4-unicorn"  
  
RUN apk add --no-cache --virtual .build-deps \  
ruby-dev \  
build-base \  
linux-headers \  
&& gem install unicorn \  
&& apk --purge del .build-deps  
  
COPY unicorn.conf.rb /usr/src/redmine/  
  
CMD ["unicorn_rails", "-c", "/usr/src/redmine/unicorn.conf.rb", "-E",
"production"]  

