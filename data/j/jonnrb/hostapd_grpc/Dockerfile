from jonnrb/bazel_cc as build  
add . /src  
run dbazel build //server:static  
  
from gcr.io/distroless/base  
copy \--from=build /src/bazel-bin/server/static /hostapd_grpc  
expose 8080 9090  
entrypoint ["/hostapd_grpc"]  
cmd ["-logtostderr"]  

