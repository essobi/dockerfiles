FROM alpine:3.7  
MAINTAINER Steven <s@ineva.cn>  
  
WORKDIR /app  
  
ARG VERSION=0.18.0  
RUN apk add --no-cache openssh-client tar curl && \  
curl -SL
"https://github.com/fatedier/frp/releases/download/v${VERSION}/frp_${VERSION}_linux_amd64.tar.gz"
| tar -xvz && \  
mv frp_${VERSION}_linux_amd64/* . && rmdir "frp_${VERSION}_linux_amd64" && \  
apk del openssh-client tar curl  
  
COPY entrypoint.sh /entrypoint.sh  
  
CMD ["sh", "/entrypoint.sh"]  

