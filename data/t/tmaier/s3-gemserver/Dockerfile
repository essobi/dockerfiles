FROM alpine:latest  
MAINTAINER Tobias Maier <tobias.maier@baucloud.com>  
  
RUN apk add --no-cache \  
ca-certificates \  
groff \  
less \  
python \  
ruby  
  
RUN echo 'gem: --no-document' >> /etc/gemrc  
  
RUN \  
apk add --no-cache --virtual build-dependencies \  
py-pip \  
&& pip install awscli \  
&& gem install builder \  
&& apk del build-dependencies  
  
COPY bin/* /usr/local/bin/  
  
WORKDIR /workdir  
  
CMD sh  

