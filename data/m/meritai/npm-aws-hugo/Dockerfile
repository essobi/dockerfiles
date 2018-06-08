FROM alpine:3.7  
MAINTAINER Nafis Zebarjadi <nafisto@gmail.com>  
  
# Install packages needed to build  
RUN apk add --update --no-cache \  
nodejs \  
bash \  
ca-certificates \  
curl \  
py-pygments \  
python \  
py-pip \  
wget \  
&& pip install -U awscli  
  
ENV HUGO_VERSION 0.39  
ENV HUGO_BINARY hugo_0.39_Linux-64bit  
  
# Download and Install hugo  
RUN mkdir /usr/local/hugo  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/hugo/  
RUN tar xzf /usr/local/hugo/${HUGO_BINARY}.tar.gz -C /usr/local/hugo/ \  
&& ln -s /usr/local/hugo/hugo /usr/local/bin/hugo \  
&& rm /usr/local/hugo/${HUGO_BINARY}.tar.gz  
EXPOSE 1313  
CMD hugo version

