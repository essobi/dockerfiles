FROM alpine:3.4  
ARG PROJECT=special-reports-rw-neo4j  
  
ADD . /${PROJECT}/  
  
RUN apk add --no-cache bash \  
&& apk --no-cache --virtual .build-dependencies add git go \  
&& cd ${PROJECT} \  
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
&& REPO_ROOT="github.com/Financial-Times/" \  
&& REPO_PATH="$REPO_ROOT/${PROJECT}" \  
&& mkdir -p $GOPATH/src/${REPO_ROOT} \  
&& mv ${PROJECT} $GOPATH/src/${REPO_ROOT} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get ./... \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& echo ${LDFLAGS} \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv ${PROJECT} / \  
&& apk del .build-dependencies \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD [ "/special-reports-rw-neo4j" ]  

