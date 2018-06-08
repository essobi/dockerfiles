FROM google/cloud-sdk  
  
RUN echo 'alias ls="ls --color=auto"' >> ~/.bashrc  
RUN echo 'alias ll="ls -halF"' >> ~/.bashrc  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
git \  
curl \  
mercurial \  
make \  
binutils \  
bison \  
gcc \  
build-essential \  
netcat \  
unzip  
  
# Install golang  
ENV GOLANG_VERSION 1.6.2  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
e40c36ae71756198478624ed1bb4ce17597b3c19d243f3f0899bb5740d56212a  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  
  
COPY go-wrapper /usr/local/bin/  
  
# Google App Engine  
RUN wget -O appengine.zip https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-1.9.40.zip  
RUN unzip -q appengine.zip -d /appengine && \  
rm -f appengine.zip  
ENV PATH /appengine/go_appengine:$PATH  

