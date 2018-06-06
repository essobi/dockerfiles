FROM alpine:3.3  
ADD . /subjects-transformer/  
ADD *.go .git /subjects-transformer/  
RUN apk add --update bash \  
&& apk --update add git go bzr \  
&& cd subjects-transformer \  
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
&& REPO_PATH="github.com/Financial-Times/subjects-transformer" \  
&& mkdir -p $GOPATH/src/${REPO_PATH} \  
&& cp -r subjects-transformer/* $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get -t ./... \  
&& echo ${LDFLAGS} \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv subjects-transformer /app \  
&& apk del go git bzr\  
&& rm -rf $GOPATH /var/cache/apk/*  
CMD [ "/app" ]

