FROM alpine:3.7  
WORKDIR /home/goldfish/app/  
  
RUN addgroup -S goldfish && \  
adduser -S -G goldfish goldfish && \  
chown -R goldfish:goldfish /home/goldfish  
  
ENV GOLDFISH_VERSION=v0.9.0  
RUN apk --no-cache add \  
\--virtual build-dependencies \  
curl && \  
apk --no-cache add \  
jq \  
curl \  
ca-certificates && \  
curl -L -o goldfish
https://github.com/Caiyeon/goldfish/releases/download/$GOLDFISH_VERSION/goldfish-
linux-amd64 && \  
chmod +x ./goldfish && \  
apk del build-dependencies  
  
COPY ./config.hcl ./config.hcl  
  
COPY ./start.sh ./start.sh  
  
RUN chmod +x ./start.sh  
  
EXPOSE 8000  
# Start and initialize Goldfish against Vault  
CMD ./start.sh  
  
USER goldfish  

