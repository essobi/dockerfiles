FROM 32bit/debian:jessie  
  
ENV GO_VERSION=1.8.3 NODE_VERSION=7.10.0 PREFIX=/usr BUILD_TAGS=builtin_assets
GOPATH=/usr/lib/go GOBIN=/usr/lib/go/bin  
  
RUN echo "deb http://deb.debian.org/debian jessie-backports main"
>>/etc/apt/sources.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y -t jessie-backports \  
build-essential \  
ca-certificates \  
curl \  
git \  
golang-go \  
librrd-dev \  
pandoc \  
xz-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install -y nodejs --no-install-recommends  
  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/go/bin:/usr/local/node/bin:/usr/lib/go/bin  
  
WORKDIR /  
RUN git clone https://github.com/facette/facette  
WORKDIR /facette  
  
RUN go get github.com/jteeuwen/go-bindata && cd
${GOPATH}/src/github.com/jteeuwen/go-bindata/go-bindata && go install  
  
RUN make && \  
make install && \  
install -D docs/examples/facette.yaml /etc/facette/facette.yaml && \  
useradd -r -m -u 12003 -s /usr/sbin/nologin -d /var/lib/facette facette && \  
sed -i -r \  
-e 's/listen: localhost:12003/listen: :12003/' \  
-e 's/path: data.db/path: \/var\/lib\/facette\/data.db/' \  
-e 's/assets_dir: assets/assets_dir: \/usr\/share\/facette\/assets/' \  
/etc/facette/facette.yaml && \  
rm -rf /facette  
  
WORKDIR /  
  
VOLUME /var/lib/facette  
  
USER root  
ADD ./etc/facette/* /etc/facette/  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 12003  
USER 12003  
ENTRYPOINT ["/entrypoint.sh"]  
  

