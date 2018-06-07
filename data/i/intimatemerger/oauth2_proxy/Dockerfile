FROM alpine:3.5  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
ARG VERSION=2.1  
ARG ARCH=linux-amd64.go1.6  
RUN apk add --no-cache curl ca-certificates && \  
curl -sSL
"https://github.com/bitly/oauth2_proxy/releases/download/v${VERSION}/oauth2_proxy-${VERSION}.${ARCH}.tar.gz"
| tar -xvz -C /tmp && \  
mv /tmp/oauth2_proxy-${VERSION}.${ARCH}/oauth2_proxy /usr/bin/oauth2_proxy &&
\  
rm -rf /tmp/* && \  
apk del curl && \  
echo fine > /healthcheck  
  
EXPOSE 4180  
ENTRYPOINT ["/usr/bin/oauth2_proxy", "-skip-auth-regex=/healthcheck", "-http-
address=0.0.0.0:4180"]  

