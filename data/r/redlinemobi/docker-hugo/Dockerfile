FROM golang  
  
RUN go get github.com/spf13/hugo  
  
ADD data /data  
  
VOLUME ["/data"]  
  
RUN git clone https://github.com/spf13/hugoThemes /data/themes  
  
ENTRYPOINT /go/bin/hugo server -s /data --watch  
  
EXPOSE 1313  

