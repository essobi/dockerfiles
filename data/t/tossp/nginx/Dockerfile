FROM alpine:edge  
  
LABEL maintainer="TossPig <docker@TossP.com>" \  
version="1.0.2" \  
description="nginx服务"  
  
ENV TIMEZONE Asia/Shanghai  
  
# RUN echo -e
"http://mirrors.aliyun.com/alpine/edge/main/\nhttp://mirrors.aliyun.com/alpine/edge/community/"
> /etc/apk/repositories  
RUN apk update && \  
apk upgrade && \  
apk add openssl nginx && \  
apk add tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
mkdir -p /run/nginx && \  
apk del tzdata && \  
rm -rf /var/cache/apk/* && \  
  
# 群晖HTTP用户信息  
adduser -u 1023 -D -H -k /sbin/nologin http && \  
adduser -u 994 -D -H -k /sbin/nologin httpyss && \  
echo '#!/bin/sh' > /ENTRYPOINT.sh && \  
echo 'cp -rf /etc/nginx/* /def_conf' >> /ENTRYPOINT.sh && \  
echo 'nginx -c /conf/nginx.conf -t' >> /ENTRYPOINT.sh && \  
echo 'nginx -c /conf/nginx.conf' >> /ENTRYPOINT.sh && \  
#cat /ENTRYPOINT.sh && \  
chmod 755 /ENTRYPOINT.sh  
  
VOLUME ["/var/log/nginx","/def_conf","/conf","/hosts","/tsrun"]  
  
EXPOSE 80 443  
#ENTRYPOINT ["env"]  
#CMD ["cat","/etc/nginx/nginx.conf"]  
CMD ["/ENTRYPOINT.sh"]  

