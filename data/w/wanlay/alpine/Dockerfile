FROM alpine:3.6  
MAINTAINER wanlay <wlwanlay@gmail.com>  
  
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g'
/etc/apk/repositories && \  
apk update && apk add --no-cache bash  
  
CMD ["/bin/bash"]  

