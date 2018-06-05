FROM ubuntu:16.04  
# Install dependencies  
RUN apt-get update && apt-get install -y wget curl git  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN add-apt-repository ppa:ubuntugis/ppa  
RUN apt-get update && apt-get install -y gdal-bin libgdal-dev python-gdal  
  
# Install Go  
RUN apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.7.5  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
2e4dd6c44f0693bef4e7b46cc701513d74c3cc44f2419bf519d7868b12931ac3  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
# Install Tyler  
RUN touch .env  
  
ENV PKG_CONFIG_PATH /go/src/github.com/botlink/botlink-
tyler/vendor/github.com/botlink/gdal  
ENV CGO_CFLAGS -I/go/src/github.com/botlink/botlink-
tyler/vendor/github.com/botlink/gdal  
  
COPY . /go/src/github.com/botlink/botlink-tyler  
WORKDIR /go/src/github.com/botlink/botlink-tyler  
  
RUN go get github.com/joho/godotenv/cmd/godotenv  
  
EXPOSE 3000  
RUN go build  
  
CMD godotenv -f /go/src/github.com/botlink/botlink-tyler/.env ./botlink-tyler  

