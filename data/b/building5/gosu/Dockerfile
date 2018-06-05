FROM alpine  
  
ENV GOSU_VERSION 1.10  
RUN apk update && \  
apk add gnupg  
  
RUN wget -q -O /gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" &&
\  
wget -q -O /gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc"  
  
# If you're diligent, you'll check this key against what's listed on  
# https://github.com/tianon/gosu  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN gpg --batch --verify /gosu.asc /gosu  
RUN chmod +x /gosu  
  
FROM scratch  
LABEL maintainer="David M. Lee, II <leedm777@yahoo.com>"  
COPY \--from=0 /gosu /  

