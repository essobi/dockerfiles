FROM python:3-alpine  
LABEL maintainer="lalung.alexandre@gmail.com"  
  
RUN apk --update add git openssh && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
WORKDIR /indy  
  
COPY indy /usr/local/bin/  
  
USER 1000:1000  
ENTRYPOINT [ "indy" ]  
CMD ["--help"]  

