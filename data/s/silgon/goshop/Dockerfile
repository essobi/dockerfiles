# usage:  
# docker run --rm -p 9000:9000 silgon/goshop  
# access: https://localhost:9000  
FROM golang:1.5  
ENV PORT 9000  
ENV GOPATH /go  
  
RUN go get github.com/rofrol/goshop  
  
RUN apt-get update && apt-get install -y \  
unzip \  
sqlite3 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd $GOPATH/src/github.com/rofrol/goshop && \  
wget http://foundation.zurb.com/cdn/releases/foundation-5.0.3.zip && \  
unzip foundation-5.0.3.zip -d static/foundation &&\  
rm foundation-5.0.3.zip  
  
RUN cd $GOPATH/src/github.com/rofrol/goshop && \  
mkdir tls && cd tls &&\  
openssl req -nodes -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -subj
"/CN=localhost" &&\  
cd $GOPATH/src/github.com/rofrol/goshop/db && \  
sqlite3 app.db < schema.sql && \  
cd .. &&\  
go get .  
  
EXPOSE $PORT  
  
CMD cd $GOPATH/src/github.com/rofrol/goshop && goshop  

