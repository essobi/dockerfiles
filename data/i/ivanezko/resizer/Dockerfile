FROM golang:1.5  
RUN set -e ; apt-get update ; \  
apt-get install -y --no-install-recommends \  
libmagickwand-dev \  
imagemagick \  
graphicsmagick ; \  
apt-get clean ; \  
rm -rf /var/lib/apt/lists/* ; \  
cat /usr/share/zoneinfo/Europe/Kiev > /etc/localtime ; \  
echo 'Europe/Kiev' > /etc/timezone  
  
RUN mkdir -p /go/src/resizer  
WORKDIR /go/src/resizer  
  
COPY . /go  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]

