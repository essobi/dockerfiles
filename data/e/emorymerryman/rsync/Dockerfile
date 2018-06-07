FROM alpine:3.4  
RUN \  
apk update && \  
apk upgrade && \  
apk add rsync && \  
apk add openssh && \  
true  
ENTRYPOINT ["rsync"]  
CMD ["--help"]

