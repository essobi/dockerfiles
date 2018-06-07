FROM alpine:3.7  
RUN apk add --no-cache curl  
RUN curl -L
https://bintray.com/jfrog/helm/download_file?file_path=2.7.2-j%2Flinux-
amd64%2Fhelm \  
\--output /usr/bin/helm && chmod +x /usr/bin/helm  
  
RUN helm init --client-only  
  
ENTRYPOINT ["/usr/bin/helm"]  

