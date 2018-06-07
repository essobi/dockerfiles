from golang:1.9.2-alpine3.7 as build-env  
env pkg github.com/mcluseau/kingress  
add . ${GOPATH}/src/${pkg}  
run cd ${GOPATH}/src/${pkg} \  
&& go vet ./... \  
&& go test ./... \  
&& go install  
  
from alpine:3.7  
entrypoint ["/kingress"]  
copy \--from=build-env /go/bin/kingress /  

