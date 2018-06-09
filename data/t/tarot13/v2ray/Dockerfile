FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
ARG V2RAY_VER=3.22  
RUN apk add --no-cache bash curl nano ca-certificates && \  
curl -L "https://github.com/v2ray/v2ray-
core/releases/download/v${V2RAY_VER}/v2ray-linux-64.zip" -o /tmp/v2ray.zip &&
\  
unzip /tmp/v2ray.zip -d /tmp/ && \  
mv /tmp/v2ray-v${V2RAY_VER}-linux-64/v2ray /usr/local/bin/v2ray && \  
mv /tmp/v2ray-v${V2RAY_VER}-linux-64/v2ctl /usr/local/bin/v2ctl && \  
chmod +x /usr/local/bin/v2ray && \  
chmod +x /usr/local/bin/v2ctl && \  
rm -rf /tmp/v2ray* && \  
curl -O https://raw.githubusercontent.com/tests-always-included/mo/master/mo
&& \  
mv mo /usr/local/bin && \  
chmod +x /usr/local/bin/mo  
  
ENTRYPOINT ["/usr/local/bin/v2ray"]  
  
CMD ["-config", "/etc/v2ray/config.json"]

