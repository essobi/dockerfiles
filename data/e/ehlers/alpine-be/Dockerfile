# nicer alpine image  
  
FROM alpine  
  
RUN set -ex \  
#  
# install dumb-init and nodnsd  
#  
&& apk add --update-cache dumb-init \  
&& apk add --virtual build-deps wget ca-certificates libcap \  
&& mkdir -p /usr/local/sbin \  
&& cd /usr/local/sbin \  
&& wget -q -O nodnsd
https://github.com/ehlers/nodnsd/releases/download/v0.1/nodnsd_0.1_amd64 \  
&& chmod 755 nodnsd \  
&& setcap cap_net_bind_service=+ep nodnsd \  
&& cd - \  
&& apk del build-deps \  
&& rm -rf /var/cache/apk/* \  
#  
# startup script  
#  
&& echo -e '\  
\x23!/bin/sh\n\  
[ $$ -eq 1 ] && exec dumb-init -r 15:1 -- "$0" "$@"\n\  
\n\  
nodnsd\n\  
\n\  
if [ $# -gt 0 ]; then\n\  
exec "$@"\n\  
else\n\  
cd; exec ash -i\n\  
fi' \  
> /etc/init.sh && chmod +x /etc/init.sh  
  
ENTRYPOINT [ "/etc/init.sh" ]  
VOLUME [ "/root" ]  

