FROM alpine:3.1  
#RUN echo
"http://nl.alpinelinux.org/alpine/edge/testing">>/etc/apk/repositories  
RUN apk update  
RUN apk add python-dev curl libxml2-dev libxslt-dev libffi-dev gcc musl-dev
libgcc openssl-dev  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install scrapy  
#CMD ["sh"]  
ENTRYPOINT ["/usr/bin/scrapy"]

