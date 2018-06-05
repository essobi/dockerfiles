FROM alpine:3.6  
MAINTAINER pancho horrillo <pancho@pancho.name>  
  
COPY version.go /tmp/sandbox/  
  
RUN set -e; \  
USER=ryanchapman; \  
PROJECT=go-any-proxy; \  
PACKAGES='ca-certificates git go gcc musl-dev'; \  
apk add --no-cache $PACKAGES; \  
SANDBOX=/tmp/sandbox; \  
mkdir -p "$SANDBOX"; \  
git clone \--depth 1 https://github.com/"$USER/$PROJECT".git
"$SANDBOX/$PROJECT"; \  
mv "$SANDBOX"/version.go "$SANDBOX/$PROJECT"; \  
export GOPATH="$SANDBOX/go" GOBIN=/; \  
go get github.com/zdannar/flogger; \  
go install -ldflags '-s' ."$SANDBOX/$PROJECT"; \  
rm -rf "$SANDBOX"; \  
apk del $PACKAGES  
  
EXPOSE 53  
ENTRYPOINT ["/go-any-proxy"]  

