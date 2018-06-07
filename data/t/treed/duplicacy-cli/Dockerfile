FROM frolvlad/alpine-glibc  
  
RUN apk --no-cache add ca-certificates  
  
ADD https://github.com/gilbertchen/duplicacy-
cli/releases/download/v1.2.5/duplicacy_linux_x64_1.2.5 /duplicacy  
RUN chmod +x /duplicacy  
WORKDIR /backup  
  
ENTRYPOINT ["/duplicacy"]  

