FROM alpine:3.5  
COPY . /gopath/src/github.com/Financial-Times/elasticsearch-reindexer/  
  
RUN apk --update add git go libc-dev ca-certificates \  
&& cd /gopath/src/github.com/Financial-Times/elasticsearch-reindexer \  
&& export GOPATH=$(pwd | sed "s/\/src\/github\\.com\/.*$//") \  
&& BUILDINFO_PACKAGE="github.com/Financial-Times/elasticsearch-
reindexer/vendor/github.com/Financial-Times/service-status-go/buildinfo." \  
&& VERSION="version=$(git describe --tag --always 2> /dev/null)" \  
&& DATETIME="dateTime=$(date -u +%Y%m%d%H%M%S)" \  
&& REPOSITORY="repository=$(git config --get remote.origin.url)" \  
&& REVISION="revision=$(git rev-parse HEAD)" \  
&& BUILDER="builder=$(go version)" \  
&& LDFLAGS="-X '"${BUILDINFO_PACKAGE}$VERSION"' -X
'"${BUILDINFO_PACKAGE}$DATETIME"' -X '"${BUILDINFO_PACKAGE}$REPOSITORY"' -X
'"${BUILDINFO_PACKAGE}$REVISION"' -X '"${BUILDINFO_PACKAGE}$BUILDER"'" \  
&& echo $LDFLAGS \  
&& go get -u github.com/kardianos/govendor \  
&& $GOPATH/bin/govendor sync \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv elasticsearch-reindexer /elasticsearch-reindexer \  
&& mv startup.sh /startup.sh \  
&& cd / \  
&& chmod +x startup.sh \  
&& apk del go libc-dev \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
ONBUILD COPY . /index-mapping/  
  
ONBUILD RUN cd /index-mapping \  
&& echo "$(git describe --tag --always 2> /dev/null)" > /mapping.version \  
&& cp /index-mapping/mapping.json / \  
&& if [ -f /index-mapping/alias-filter.json ]; then cp /index-mapping/alias-
filter.json / ; fi \  
&& apk del git \  
&& rm -rf /index-mapping  
  
CMD [ "/startup.sh" ]  

