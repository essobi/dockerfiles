FROM alpine:latest  
LABEL maintainer "Claudio Rodriguez <claudio.rdgz@gmail.com>"  
  
ENV HADOLINT_VERSION=1.6.5  
WORKDIR /data  
  
RUN apk add --update ca-certificates openssl && \  
wget -O hadolint
"https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-
Linux-x86_64" && \  
chmod +x hadolint && \  
mv hadolint /bin && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["sh"]  

