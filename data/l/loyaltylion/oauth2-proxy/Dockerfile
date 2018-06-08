FROM alpine:latest  
  
RUN apk add --no-cache curl tini  
  
ENV TAG v2.2  
ENV RELEASE oauth2_proxy-2.2.0.linux-amd64.go1.8.1  
RUN set -x \  
&& curl -SLO
"https://github.com/bitly/oauth2_proxy/releases/download/$TAG/$RELEASE.tar.gz"
\  
&& tar -xzf "$RELEASE.tar.gz" -C /usr/local/bin --strip-components=1 \  
&& rm "$RELEASE.tar.gz"  
  
EXPOSE 4180  
ENV OAUTH2_PROXY_CLIENT_ID='' \  
OAUTH2_PROXY_CLIENT_SECRET=''  
ENTRYPOINT [ "tini", "--", "oauth2_proxy" ]  
  
CMD [ "-http-address=0.0.0.0:4180", \  
"-upstream=http://127.0.0.1:8000", \  
"-email-domain=example.com" ]  

