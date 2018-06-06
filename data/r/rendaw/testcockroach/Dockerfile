from golang:1.10.2 as build  
run apt-get update && apt-get -y upgrade  
run apt-get install -y build-essential  
run apt-get install -y git  
run apt-get install -y cmake  
run apt-get install -y autoconf  
run apt-get install -y libncurses-dev  
run curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install
-y nodejs  
run npm install -g yarn  
arg version=v2.0.2  
run (\  
git clone \--recurse-submodules https://github.com/cockroachdb/cockroach.git
/go/src/github.com/cockroachdb/cockroach && \  
true)  
run (\  
cd /go/src/github.com/cockroachdb/cockroach && \  
git config user.name x && \  
git config user.email x@example.com && \  
git checkout ${version} && \  
git submodule update --recursive && \  
sed -i 's/6.7.3/6.8.6","espree":"","escodegen":"","estraverse":"/g'
pkg/ui/package.json && \  
git commit -a -m "<internal for build>" && \  
git tag -f ${version} && \  
make bin/.bootstrap && \  
make .buildinfo/tag && \  
cp bin/* $(GOPATH)/bin && \  
grep 6.8.6 pkg/ui/package.json && \  
make buildoss && \  
true)  
add . /go/src/github.com/micromicromicro/testcockroach  
run (\  
cd /go/src/github.com/micromicromicro/testcockroach && \  
go install -ldflags "-X
github.com/cockroachdb/cockroach/pkg/build.tag="${version} && \  
true)  
from golang:1.10.2  
copy \--from=build /go/bin/testcockroach .  
copy \--from=build /go/src/github.com/cockroachdb/cockroach/cockroach .  
cmd ./testcockroach  
entrypoint []  
expose 8080  
expose 26257

