FROM alpine:3.4  
ADD *.go .git /methode-publish-handler/  
ADD ./vanities/*.go /methode-publish-handler/vanities/  
  
RUN apk --update add git go \  
&& export GOPATH=/gopath \  
&& REPO_PATH="github.com/Financial-Times/methode-publish-handler" \  
&& cd methode-publish-handler \  
&& echo "Setting up environment" \  
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
&& echo $LDFLAGS \  
&& mkdir -p $GOPATH/src/${REPO_PATH} \  
&& mv * $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& echo "Getting GO packages" \  
&& go get -t ./... \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv methode-publish-handler /methode-publish-handler-app \  
&& apk del go git \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD exec /methode-publish-handler-app \  
\--app-name="$APP_NAME" \  
\--app-port="$APP_PORT" \  
\--notifier="$NOTIFIER_NAME" \  
\--notifier-url="$NOTIFIER_URL" \  
\--notifier-panic-guide="$NOTIFIER_PANIC_GUIDE" \  
\--notifier-health-url="$NOTIFIER_HEALTH_URL"  

