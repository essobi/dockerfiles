FROM alpine:3.6  
MAINTAINER Adam Dodman <"adam.dodman@gmx.com">  
  
COPY . /quotedb/  
  
RUN apk add --no-cache python3 py3-pip tini gcc python3-dev libc-dev ca-
certificates libffi-dev \  
&& pip3 install -r /quotedb/requirements.txt \  
&& ln -s /quotedb/adduser.py /usr/bin/quote-adduser  
  
VOLUME ["/config"]  
  
CMD ["/sbin/tini","--","python3","-u","/quotedb/main.py","-c","/config"]  

