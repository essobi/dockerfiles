FROM alpine:latest  
LABEL maintainer="Vincent Faliès <vincent@vfac.fr>"  
  
RUN apk --update add ca-certificates && \  
apk add -U \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /app/ssl  
  
ADD certificate.sh /app/  
ADD regenerate_certificate.sh /app/  
  
WORKDIR /app

