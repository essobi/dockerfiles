FROM alpine:3.4  
MAINTAINER Chao Shen <shen218@gmail.com>  
ADD src /  
RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.3/main >
/etc/apk/repositories && \  
echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
#RUN echo https://mirrors.ustc.edu.cn/alpine/v3.4/main > /etc/apk/repositories
&& \  
# echo https://mirrors.ustc.edu.cn/alpine/edge/community >>
/etc/apk/repositories  
RUN apk add --no-cache curl \  
&& curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz \  
| tar xvzf - -C / \  
&& apk del --no-cache curl  
  
CMD ["/init"]  
  

