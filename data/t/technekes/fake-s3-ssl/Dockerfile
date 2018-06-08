FROM alpine:3.6  
  
ARG HOST_NAME=s3.amazonaws.com  
  
ENV FAKES3_VERSION 1.2.0  
  
WORKDIR /var/lib/fakes3/data  
VOLUME /var/lib/fakes3/data  
  
EXPOSE 443  
  
RUN \  
apk --no-cache add ca-certificates openssl ruby ruby-io-console && \  
gem install --no-rdoc --no-ri fakes3 -v ${FAKES3_VERSION} && \  
rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

