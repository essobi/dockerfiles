FROM alpine:latest  
  
RUN apk add --no-cache ca-certificates wget;\  
wget
https://github.com/gohugoio/hugo/releases/download/v0.26/hugo_0.26_Linux-64bit.tar.gz
;\  
tar xf hugo_0.26_Linux-64bit.tar.gz ;\  
rm hugo_0.26_Linux-64bit.tar.gz ;\  
apk del wget ;\  
mv hugo /usr/bin/;\  
apk add --no-cache py-pygments openssh-client git;\  
mkdir build scratch  
  
COPY scripts/entry.sh /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  

