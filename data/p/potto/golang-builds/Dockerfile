FROM golang:1.8.1  
  
MAINTAINER Paul Otto <paul@ottoops.com>  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# ENV for Glide  
ENV GLIDE_VERSION v0.12.3  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.tar.gz  
ENV GLIDE_DOWNLOAD_SHA256
0e2be5e863464610ebc420443ccfab15cdfdf1c4ab63b5eb25d1216900a75109  
ENV PATH $PATH:/usr/local/glide/linux-amd64  
  
RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.tar.gz \  
&& echo "$GLIDE_DOWNLOAD_SHA256 glide.tar.gz" | sha256sum -c \- \  
&& mkdir -p /usr/local/glide \  
&& tar -C /usr/local/glide -xzf glide.tar.gz \  
&& rm glide.tar.gz \  
&& go get -u github.com/Masterminds/glide-report \  
&& go get -u github.com/sgotti/glide-vc \  
&& go get -u github.com/ngdinhtoan/glide-cleanup \  
&& go get github.com/mitchellh/gox \  
&& go get github.com/smartystreets/goconvey \  
&& go get github.com/golang/lint/golint \  
&& go get honnef.co/go/tools/cmd/gosimple \  
&& go get github.com/mdempsky/unconvert \  
&& go get github.com/opennota/check/cmd/structcheck \  
&& go get github.com/opennota/check/cmd/varcheck \  
&& go get github.com/HewlettPackard/gas  

