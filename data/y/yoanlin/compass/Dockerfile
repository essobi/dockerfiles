FROM alpine:3.7  
WORKDIR /  
RUN apk update  
RUN apk add ruby  
RUN apk add -vv --virtual .build-dep ruby-dev build-base libffi-dev \  
&& gem install --no-document listen sass compass \  
&& apk del .build-dep \  
&& rm -rf /var/cache/apk  
# vim:filetype=dockerfile:  

