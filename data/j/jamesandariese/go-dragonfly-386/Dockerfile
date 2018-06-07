FROM debian:8  
RUN apt-get update && apt-get install -y git && git clone -q
https://go.googlesource.com/go /gosrc && (cd /gosrc && git checkout -q
release-branch.go1.4) && rm -rf /gosrc/.git && rm -rf /var/lib/apt/lists/*  
  
ENV GOROOT=/gosrc  
ENV GOPATH=/go  
ENV
PATH=/go/bin:/gosrc/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV CGO_ENABLED=0  
VOLUME ["/go"]  
ENTRYPOINT ["/gosrc/bin/go"]  
CMD ["help"]  
ENV GOARCH=386  
ENV GOOS=dragonfly  
  
RUN apt-get update && apt-get install -y build-essential && (cd /gosrc/src &&
./make.bash --dist-tool /dist) && eval $(/dist env -p || echo FAIL=true) && [
x"$FAIL" != xtrue ] && /dist bootstrap $GO_DISTFLAGS -v &&
"$GOTOOLDIR"/go_bootstrap clean -i std && CC=$CC GOOS=$GOHOSTOS
GOARCH=$GOHOSTARCH "$GOTOOLDIR"/go_bootstrap install -ccflags "$GO_CCFLAGS"
-gcflags "$GO_GCFLAGS" -ldflags "$GO_LDFLAGS" -v std && CC=$CC_FOR_TARGET
"$GOTOOLDIR"/go_bootstrap install $GO_FLAGS -ccflags "$GO_CCFLAGS" -gcflags
"$GO_GCFLAGS" -ldflags "$GO_LDFLAGS" -v std && rm -f "$GOTOOLDIR"/go_bootstrap
&& rm /dist && dpkg -P build-essential && apt-get autoremove -y --purge &&
dpkg -P perl-modules debconf-i18n libtext-iconv-perl libparse-debianchangelog-
perl && apt-get clean && apt-get autoremove -y --purge && rm -rf /gosrc/.git
/gosrc/bin/[a-fh-z]* /var/lib/apt/lists/* && [ x"$GOOS $GOARCH" != x"$GOHOSTOS
$GOHOSTARCH" ] && rm -rf /gosrc/pkg/"$GOHOSTOS"_"$GOHOSTARCH" || true  
  

