FROM alpine:3.6  
MAINTAINER Koichi Ashizaki  
  
RUN apk --no-cache add \  
g++ \  
&& apk --no-cache add --virtual build-dependencies \  
git \  
autoconf \  
automake \  
make  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/torognes/vsearch.git \  
&& cd vsearch \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& ln -s /usr/src/vsearch /usr/bin/vsearch \  
&& apk del build-dependencies \  
&& rm -rf vsearch  
  
CMD ["vsearch"]

