FROM alpine  
MAINTAINER Ivan Yaroslavov Stefanov <ivan.yaroslavov@vne.io>  
  
ARG SRC_FOLDER=/opt/vne-accounting-src  
  
COPY . $SRC_FOLDER  
  
RUN cd $SRC_FOLDER \  
&& apk update \  
&& apk add build-base \  
&& apk add libev-dev \  
&& apk add hiredis-dev \  
&& make \  
&& apk del build-base  
  
WORKDIR $SRC_FOLDER  
CMD ./accounting  

