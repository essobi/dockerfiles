FROM alpine:3.6  
  
LABEL maintainer="mritd <mritd1234@gmail.com>"  
  
ENV TZ 'Asia/Shanghai'  
  
ENV V2RAY_VERSION v3.21  
  
RUN apk upgrade --update \  
&& apk add \  
bash \  
tzdata \  
curl \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& mkdir -p \  
/var/log/v2ray \  
/tmp/v2ray \  
/etc/joeyv/ \  
/usr/local/bin/joeyv/ \  
&& curl -L -H "Cache-Control: no-cache" -o /tmp/v2ray/v2ray.zip \  
https://github.com/v2ray/v2ray-core/releases/download/${V2RAY_VERSION}/v2ray-
linux-64.zip \  
&& unzip /tmp/v2ray/v2ray.zip -d /tmp/v2ray/ \  
&& mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/v2ray
/usr/local/bin/joeyv/joeyv \  
&& mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/v2ctl
/usr/local/bin/joeyv/v2ctl \  
&& mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/geoip.dat
/usr/local/bin/joeyv/geoip.dat \  
&& mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/geosite.dat
/usr/local/bin/joeyv/geosite.dat \  
&& mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/vpoint_vmess_freedom.json
/etc/joeyv/config.json \  
&& chmod +x /usr/local/bin/joeyv/joeyv \  
&& chmod +x /usr/local/bin/joeyv/v2ctl \  
&& rm -rf /tmp/v2ray /var/cache/apk/*  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENV PATH /usr/local/bin/joeyv:$PATH  
  
ENTRYPOINT ["/entrypoint.sh"]  

