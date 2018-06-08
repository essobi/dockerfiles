FROM alpine  
# install sass and inotify  
RUN apk update \  
&& apk add --no-cache git build-base libstdc++ inotify-tools\  
&& git clone https://github.com/sass/sassc\  
&& cd /sassc/ \  
&& git clone https://github.com/sass/libsass\  
&& SASS_LIBSASS_PATH=/sassc/libsass make \  
&& mv bin/sassc /usr/bin/sass\  
&& rm -rf /sassc\  
&& apk del git build-base  
  
LABEL maintainer="pablofelix@coomars.com"\  
version="1.1"\  
description="sass image with shell watcher"  
#copy to /usr/bin to have access in all directories  
COPY $PWD/watch.sh /usr/bin/watch  
  
ENTRYPOINT ["watch"]  

