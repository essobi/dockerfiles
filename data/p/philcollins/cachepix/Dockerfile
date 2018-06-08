FROM golang:1.8  
MAINTAINER Steve Salevan <steve.salevan@gmail.com>  
  
ENV GLIDE_VERSION v0.12.3  
VOLUME /etc/cachepix /var/lib/cachepix  
  
RUN apt-get update \  
&& apt-get install -y unzip --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.zip  
  
RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.zip \  
&& unzip glide.zip linux-amd64/glide \  
&& mv linux-amd64/glide /usr/local/bin \  
&& rm -rf linux-amd64 \  
&& rm glide.zip  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb  
RUN dpkg -i dumb-init_*.deb  
  
WORKDIR /go/src/github.com/ssalevan/cachepix  
  
ENV GLIDE_HOME /go/src/github.com/ssalevan/cachepix  
  
COPY . .  
RUN glide install \  
&& go-wrapper install  
  
ENTRYPOINT ["dumb-init", "/go/src/github.com/ssalevan/cachepix/docker-run.sh"]  

