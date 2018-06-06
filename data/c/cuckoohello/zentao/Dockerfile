FROM alpine  
ENV GLIBC_VERSION 2.25-r0  
  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
  
RUN apk add --update --no-cache curl tar ca-certificates jq && \  
curl -LOsS https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
curl -LsS -o /etc/apk/keys/sgerrand.rsa.pub
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub && \  
apk add glibc-${GLIBC_VERSION}.apk && \  
rm /etc/apk/keys/sgerrand.rsa.pub glibc-${GLIBC_VERSION}.apk  
  
RUN mkdir -p /opt/ && curl -fsSL
http://dl.cnezsoft.com/zentao/9.2.1/ZenTaoPMS.9.2.1.zbox_64.tar.gz | tar xzf -
-C /opt/ && cp -rf /opt/zbox/data/mysql/ /opt/zbox/data/mysql.sav  
  
EXPOSE 80  
COPY entrypoint.sh /  
COPY docker-compose.yml /  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

