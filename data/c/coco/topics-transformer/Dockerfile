FROM alpine:3.3  
ADD . /topics-transformer/  
ADD *.go .git /topics-transformer/  
RUN apk add --update bash \  
&& apk --update add git go bzr \  
&& cd topics-transformer \  
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
&& REPO_PATH="github.com/Financial-Times/topics-transformer" \  
&& mkdir -p $GOPATH/src/${REPO_PATH} \  
&& cp -r topics-transformer/* $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get -t ./... \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& echo ${LDFLAGS} \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv topics-transformer /app \  
&& apk del go git bzr\  
&& rm -rf $GOPATH /var/cache/apk/*  
CMD [ "/app" ]

