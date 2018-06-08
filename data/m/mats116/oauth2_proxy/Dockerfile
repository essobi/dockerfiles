FROM alpine:3.3  
  
# change timezone  
RUN apk update \  
&& apk add tzdata \  
&& cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& apk del tzdata  
  
# install oauth2_proxy from GitHub  
ENV VERSION=2.0.1  
RUN apk add openssl util-linux \  
&& wget
"https://github.com/bitly/oauth2_proxy/releases/download/v${VERSION}/oauth2_proxy-${VERSION}.linux-
amd64.go1.4.2.tar.gz" \  
&& tar xvfz ./oauth2_proxy-${VERSION}.linux-amd64.go1.4.2.tar.gz \  
&& mv ./oauth2_proxy-${VERSION}.linux-amd64.go1.4.2/oauth2_proxy
/usr/local/bin/oauth2_proxy \  
&& rm -fr ./oauth2_proxy-${VERSION}.linux-amd64.go1.4.2*  
  
ENV HTTP_PORT=4180  
  
CMD /usr/local/bin/oauth2_proxy \  
\--http-address=0.0.0.0:${HTTP_PORT} \  
\--upstream=${UPSTREAM} \  
\--client-id=${CLIENT_ID} \  
\--client-secret=${CLIENT_SECRET} \  
\--cookie-secret=$(uuidgen)  

