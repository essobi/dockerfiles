from golang as build  
workdir /go/src/github.com/jonnrb/radarsign  
add . .  
run go get . \  
&& CGO_ENABLED=0 GOOS=linux go build . \  
&& mv radarsign /  
  
from gcr.io/distroless/base  
copy \--from=build /radarsign /radarsign  
entrypoint ["/radarsign"]  
cmd ["-logtostderr", "-v=1"]  

