FROM golang:1.10beta1-stretch  
LABEL maintainer "Koichi Shiraishi <zchee.io@gmail.com>"  
  
RUN set -eux \  
&& go get -u -v \  
github.com/haya14busa/reviewdog/cmd/reviewdog \  
\  
github.com/alecthomas/gometalinter \  
github.com/client9/misspell/cmd/misspell \  
github.com/GoASTScanner/gas \  
github.com/golang/lint/golint \  
github.com/gordonklaus/ineffassign \  
github.com/kisielk/errcheck \  
github.com/mdempsky/unconvert \  
github.com/mibk/dupl \  
github.com/opennota/check/cmd/aligncheck \  
github.com/opennota/check/cmd/structcheck \  
github.com/opennota/check/cmd/varcheck \  
github.com/tsenart/deadcode \  
golang.org/x/tools/cmd/goimports \  
honnef.co/go/tools/cmd/errcheck-ng \  
honnef.co/go/tools/cmd/gosimple \  
honnef.co/go/tools/cmd/keyify \  
honnef.co/go/tools/cmd/megacheck \  
honnef.co/go/tools/cmd/rdeps \  
honnef.co/go/tools/cmd/staticcheck \  
honnef.co/go/tools/cmd/structlayout \  
honnef.co/go/tools/cmd/structlayout-optimize \  
honnef.co/go/tools/cmd/structlayout-pretty \  
honnef.co/go/tools/cmd/unused \  
mvdan.cc/interfacer \  
mvdan.cc/unparam  
  
COPY entrypoint.sh /  
ENTRYPOINT /entrypoint.sh  

