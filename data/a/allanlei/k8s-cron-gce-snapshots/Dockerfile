FROM alpine:3.4  
  
ENV PATH=$PATH:/google-cloud-sdk/bin  
RUN apk --no-cache add --virtual .build-deps \  
curl && \  
curl -v -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-
cloud-sdk-128.0.0-linux-x86_64.tar.gz | tar xvz && \  
apk --no-cache add --virtual .run-deps \  
python && \  
apk del .build-deps  
CMD ["crond", "-f"]  

