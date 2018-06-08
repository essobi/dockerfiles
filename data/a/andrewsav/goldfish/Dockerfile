FROM alpine:3.6  
ENV GOLDFISH_VERSION=v0.8.0  
WORKDIR /app  
  
RUN apk --no-cache add \  
\--virtual build-dependencies \  
unzip && \  
apk --no-cache add \  
curl \  
ca-certificates && \  
curl -s -L -o goldfish
https://github.com/Caiyeon/goldfish/releases/download/$GOLDFISH_VERSION/goldfish-
linux-amd64 && \  
chmod +x ./goldfish && \  
apk del build-dependencies  
  
COPY entrypoint.sh .  
RUN chmod +x ./entrypoint.sh  
EXPOSE 8000  
CMD [ "./entrypoint.sh" ]  

