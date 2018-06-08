FROM alpine  
MAINTAINER Negash <i@negash.ru>  
  
RUN apk -U add ca-certificates python py-setuptools libstdc++  
  
RUN apk --update add --virtual build-dependencies py-pip build-base python-dev
\  
&& pip install locustio pyzmq \  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /dist  
ADD ./ /dist/  
  
EXPOSE 8089 5557 5558  
ENV URL '/'  
ENV HOST 'http://example.com'  
ENV MIN_WAIT 1000  
ENV MAX_WAIT 3000  
ENTRYPOINT /usr/bin/locust --host $HOST  
CMD ["--master"]

