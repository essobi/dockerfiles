FROM alpine:3.5  
MAINTAINER Mengz <mengz.you@outlook.com>  
  
RUN set -x \  
&& sed -i 's|http://dl-cdn.alpinelinux.org|https://mirrors.ustc.edu.cn|'
/etc/apk/repositories \  
&& apk add --no-cache openssh-client su-exec bash \  
&& mkdir -p /root/.ssh \  
&& chown 700 /root/.ssh  
  
COPY config /root/.ssh/config  
COPY start.sh /root/start.sh  
  
ENV SSH_REMOTE_USER="root" \  
SSH_REMOTE_PORT="22" \  
SSH_REMOTE_IP="127.0.0.1" \  
SSH_REMOTE_FORWORD_IP="127.0.0.1" \  
SSH_REMOTE_FORWORD_PORTS="80"  
WORKDIR /root  
  
ENTRYPOINT ["./start.sh"]  
CMD ["ssh"]  

