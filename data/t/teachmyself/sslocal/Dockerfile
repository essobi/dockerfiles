# sslocal  
FROM alpine:3.6  
  
ENV AUTHOR "teachmyself@126.com"  
  
ENV SERVER_HOST="1.1.1.1" \  
SERVER_PORT="8888" \  
PASSWORD="Passw0rd" \  
METHOD="aes-256-cfb" \  
LOCAL_PORT="1080" \  
PROXY_PORT="8118"  
  
ENV SSL_LOG "/var/log/sslocal.log"  
  
ADD . /sslocal  
  
RUN set -xue; \  
sed -i 's#^#\\##g' /etc/apk/repositories; \  
sed -i '1ihttp://mirrors.ustc.edu.cn/alpine/v3.6/main/' /etc/apk/repositories;
\  
sed -i '1ihttp://mirrors.ustc.edu.cn/alpine/v3.6/community/'
/etc/apk/repositories; \  
sed -i '1ihttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/main/'
/etc/apk/repositories; \  
sed -i '1ihttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/community/'
/etc/apk/repositories; \  
apk update && apk add \  
curl \  
py-pip \  
privoxy \  
&& \  
pip install shadowsocks && \  
cd /etc/privoxy && \  
cp config config.default && \  
grep -v '^\s*$\|^#' config.default > config && \  
sed -i "s#127.0.0.1:8118#:${PROXY_PORT}#g" config && \  
echo "forward-socks5 / 127.0.0.1:${LOCAL_PORT} ." >> config && \  
rm -rf /var/cache/apk/* ~/.cache  
  
EXPOSE ${PROXY_PORT}  
  
CMD ["sh", "-c", "sslocal -v -d start -s ${SERVER_HOST} -p ${SERVER_PORT} -k
${PASSWORD} -m ${METHOD} -l ${LOCAL_PORT} --log-file ${SSL_LOG} && privoxy
--no-daemon /etc/privoxy/config"]  

