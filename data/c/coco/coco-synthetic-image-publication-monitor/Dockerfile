FROM golang:1.8-alpine  
  
ENV PROJECT=coco-synthetic-image-publication-monitor  
COPY . /${PROJECT}-sources/  
  
RUN apk --no-cache --virtual .build-dependencies add git \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/${PROJECT}" \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
# Linking the project sources in the GOPATH folder  
&& ln -s /${PROJECT}-sources $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& BUILDINFO_PACKAGE="${ORG_PATH}/${PROJECT}/vendor/${ORG_PATH}/service-
status-go/buildinfo." \  
&& VERSION="version=$(git describe --tag --always 2> /dev/null)" \  
&& DATETIME="dateTime=$(date -u +%Y%m%d%H%M%S)" \  
&& REPOSITORY="repository=$(git config --get remote.origin.url)" \  
&& REVISION="revision=$(git rev-parse HEAD)" \  
&& BUILDER="builder=$(go version)" \  
&& LDFLAGS="-X '"${BUILDINFO_PACKAGE}$VERSION"' -X
'"${BUILDINFO_PACKAGE}$DATETIME"' -X '"${BUILDINFO_PACKAGE}$REPOSITORY"' -X
'"${BUILDINFO_PACKAGE}$REVISION"' -X '"${BUILDINFO_PACKAGE}$BUILDER"'" \  
&& echo "Build flags: $LDFLAGS" \  
&& echo "Fetching dependencies..." \  
&& go get -u github.com/kardianos/govendor \  
&& $GOPATH/bin/govendor sync \  
&& go build -ldflags="${LDFLAGS}" \  
&& mv ${PROJECT} /${PROJECT} \  
&& mv attributes.template /attributes.template \  
&& mv systemAttributes.template /systemAttributes.template \  
&& mv usageTickets.template /usageTickets.template \  
&& apk del .build-dependencies \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
WORKDIR /  
  
ENV AWS_ADDRESS s3.amazonaws.com  
ENV BUCKET_ADDRESS com.ft.imagepublish.int  
EXPOSE 8080  
  
CMD exec /coco-synthetic-image-publication-monitor -postHost=$POST_ADDRESS
-postCredentials="$POST_CREDENTIALS" -s3Host=$BUCKET_ADDRESS.$AWS_ADDRESS
-testUuid=$TEST_UUID

