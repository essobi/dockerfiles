ARG VERSION  
  
FROM nginx:alpine  
  
ENV RIOT_VERSION=${VERSION:-v0.13.4}  
RUN apk add --no-cache tar gzip curl ca-certificates && \  
echo "Download from https://github.com/vector-im/riot-
web/releases/download/${RIOT_VERSION}/riot-${RIOT_VERSION}.tar.gz" && \  
curl -L https://github.com/vector-im/riot-
web/releases/download/${RIOT_VERSION}/riot-${RIOT_VERSION}.tar.gz | tar -xz &&
\  
rm -rf /usr/share/nginx/html && \  
mv riot-${RIOT_VERSION} /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

