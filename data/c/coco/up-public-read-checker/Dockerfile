FROM alpine:3.4  
ENV SOURCE_DIR /up-public-read-checker-src  
  
ADD *.go .git $SOURCE_DIR/  
  
RUN apk add --update bash \  
&& apk --update add git go \  
&& cd $SOURCE_DIR \  
&& git fetch origin 'refs/tags/*:refs/tags/*' \  
&& BUILDINFO_PACKAGE="github.com/Financial-Times/service-status-go/buildinfo."
\  
&& VERSION="version=$(git describe --tag --always 2> /dev/null)" \  
&& DATETIME="dateTime=$(date -u +%Y%m%d%H%M%S)" \  
&& REPOSITORY="repository=$(git config --get remote.origin.url)" \  
&& REVISION="revision=$(git rev-parse HEAD)" \  
&& BUILDER="builder=$(go version)" \  
&& LDFLAGS="-X '"${BUILDINFO_PACKAGE}$VERSION"' -X
'"${BUILDINFO_PACKAGE}$DATETIME"' -X '"${BUILDINFO_PACKAGE}$REPOSITORY"' -X
'"${BUILDINFO_PACKAGE}$REVISION"' -X '"${BUILDINFO_PACKAGE}$BUILDER"'" \  
&& cd .. \  
&& export GOPATH=/gopath \  
&& REPO_PATH="github.com/Financial-Times/up-public-read-checker" \  
&& mkdir -p $GOPATH/src/${REPO_PATH} \  
&& cp -r $SOURCE_DIR/* $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get ./... \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& echo ${LDFLAGS} \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv up-public-read-checker / \  
&& apk del go git \  
&& rm -rf $GOPATH /var/cache/apk/*  
CMD [ "/up-public-read-checker" ]  

