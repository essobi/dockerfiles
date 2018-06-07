FROM alpine:latest  
MAINTAINER leky <lekyzsj@gmail.com>  
  
ENV TZ "Asia/Shanghai"  
# Official alpine mirrors: http://rsync.alpinelinux.org/alpine/MIRRORS.txt  
# Install packages  
# Since from alpine v3.3, apk --no-cache will run apk update first,  
# and rm -rf /var/cache/apk/* finally.  
RUN REPO_VERSION="$(grep -Eo '\d+(.\d+)?' /etc/apk/repositories | uniq)" \  
&& echo "http://mirrors.ustc.edu.cn/alpine/v${REPO_VERSION}/main" >
/etc/apk/repositories \  
&& echo "http://mirrors.ustc.edu.cn/alpine/v${REPO_VERSION}/community" >>
/etc/apk/repositories \  
&& apk add \--no-cache \  
tzdata \  
# Set default timezone  
&& ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} >
/etc/timezone \  
&& rm -rf /var/cache/apk/*  

