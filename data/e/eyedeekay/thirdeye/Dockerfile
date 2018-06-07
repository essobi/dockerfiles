FROM alpine:3.5  
ENV GOPATH=/home/jump/go/bin  
RUN apk update  
RUN apk add go go-tools musl-dev git make  
RUN adduser -h /home/jump/ -D jump jump  
COPY . /home/jump/  
RUN chown -R jump:jump /home/jump  
RUN chmod a+r /home/jump/etc/thirdeye/favicon.ico  
RUN chmod a+r /home/jump/etc/thirdeye/localhosts.txt  
RUN chmod a+r /home/jump/etc/thirdeye/style.css  
WORKDIR /home/jump  
RUN go get -u github.com/eyedeekay/gosam  
RUN make release  
USER jump  
CMD ./bin/thirdeye -samhost=thirdeye-host \  
-host=thirdeye-site \  
-newhosts=http://no.i2p/export/alive-hosts.txt,http://i2pjump.i2p/hosts,http://i2p-projekt.i2p/hosts.txt,http://i2p2.i2p/hosts.txt  

