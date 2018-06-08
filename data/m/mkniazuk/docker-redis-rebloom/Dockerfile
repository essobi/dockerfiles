FROM redis:4.0.2-alpine  
  
ENV REBLOOM_TAG "v1.0.0"  
RUN apk update && apk add --no-cache --virtual .build-deps make cmake g++ gcc
git  
  
RUN cd /usr/local \  
&& git clone https://github.com/RedisLabsModules/rebloom.git rebloom \  
&& cd rebloom \  
&& git checkout -b tags/$REBLOOM_TAG \  
&& make  
  
RUN apk del .build-deps  
  
CMD [ "redis-server", "--loadmodule /usr/local/rebloom/rebloom.so" ]

