FROM alpine:edge  
  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
RUN apk update \  
&& echo "apk add --no-cache python python-dev" \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& apk add --no-cache curl python python-dev \  
&& curl https://bootstrap.pypa.io/ez_setup.py | python \  
&& apk add --no-cache py-pip \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache leveldb-dev \  
&& apk add --no-cache build-base git \  
&& pip install --no-cache-dir --upgrade pip jsonrpclib irc plyvel leveldb \  
&& mkdir /app \  
&& git clone https://github.com/mazaclub/tate-server /tate-server  
  
RUN cd /tate-server \  
&& rm -rf app etc \  
&& echo "done"  
# && python setup.py install  
RUN echo Clean_up \  
&& mv /tate-server/* /app \  
&& apk del build-base git  
  
COPY ./app /app  
COPY ./etc /etc  
  
RUN adduser -S -u 1000 maza  
  
COPY tateserver-entrypoint.sh /entrypoint.sh  
  
EXPOSE 50001 50002 8000  
VOLUME ["/home/maza/.maza","/var/tate-server"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

