FROM alpine:3.5  
MAINTAINER TossPig "tse.code@TossP.com"  
  
RUN apk update && apk upgrade  
RUN apk --no-cache add nodejs python && \  
wget -O /bin/qshell http://devtools.qiniu.com/2.1.5/qshell-linux-x64 && \  
wget -O /bin/ossutil http://docs-aliyun.cn-hangzhou.oss.aliyun-
inc.com/assets/attach/50452/cn_zh/1506525299111/ossutil64 && \  
chmod a+x /bin/qshell && \  
chmod a+x /bin/ossutil && \  
mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2  
RUN npm i -g npm@5  

