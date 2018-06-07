FROM alpine:3.7  
LABEL maintainer="icyleaf <icyleaf.cn@gmail.com>"  
  
ENV ORIGINAL_REPO_URL="http://dl-cdn.alpinelinux.org" \  
MIRROR_REPO_URL="https://mirrors.ustc.edu.cn" \  
TZ="Asia/Shanghai"  
RUN REPLACE_STRING=$(echo $MIRROR_REPO_URL | sed 's/\//\\\\\//g') && \  
SEARCH_STRING=$(echo $ORIGINAL_REPO_URL | sed 's/\//\\\\\//g') && \  
sed -i "s/$SEARCH_STRING/$REPLACE_STRING/g" /etc/apk/repositories && \  
apk --update --no-cache add tzdata && \  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
apk del tzdata  

