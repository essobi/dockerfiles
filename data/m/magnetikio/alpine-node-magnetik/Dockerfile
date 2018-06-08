FROM mhart/alpine-node  
  
RUN apk add libsass \--update-cache \--repository
http://dl-3.alpinelinux.org/alpine/edge/testing \--allow-untrusted  
RUN apk add \--no-cache python  
RUN apk \--update add \--virtual build-dependencies g++ make \  
&& apk \--update \--virtual build-dependencies add libsass libsass-dev
\--update-cache \--repository http://dl-3.alpinelinux.org/alpine/edge/testing
\--allow-untrusted \  
&& npm install -g gulp node-sass bower \  
&& apk del build-dependencies  

