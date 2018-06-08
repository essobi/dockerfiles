FROM golang:1.10.0-alpine  
  
RUN apk update  
RUN apk add ca-certificates curl wget htop openssh openssl git tar netcat-
openbsd  
  
# Add database clients  
RUN apk add postgresql-client mysql-client  
  
# Install goveralls for test coverage reporting  
RUN go get github.com/mattn/goveralls  
  
# Install git-lfs  
RUN wget -qO- https://github.com/git-lfs/git-lfs/releases/download/v2.3.4/git-
lfs-linux-amd64-2.3.4.tar.gz | tar xz  
RUN mv git-lfs-*/git-lfs /usr/bin/ && rm -rf git-lfs-* && git lfs install

