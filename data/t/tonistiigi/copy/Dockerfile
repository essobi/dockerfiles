from golang:1.10-alpine AS main  
workdir /go/src/github.com/tonistiigi/copy  
copy . .  
env CGO_ENABLED=0  
run go build -o /copy -ldflags '-s -w' github.com/tonistiigi/copy/cmd/copy  
  
from gruebel/upx AS upx  
copy \--from=main /copy /copy  
run ["upx", "/copy"]  
  
from alpine AS wget  
workdir /out  
run apk add --no-cache wget  
  
from wget AS cp  
run wget http://s.minos.io/archive/bifrost/x86_64/coreutils-7.6-5.tar.gz  
run tar xvf coreutils-7.6-5.tar.gz -C /  
  
from wget AS tar  
run wget http://s.minos.io/archive/bifrost/x86_64/tar-1.23-1.tar.gz  
run tar xvf tar-1.23-1.tar.gz -C /out  
  
from wget AS gz  
run wget http://s.minos.io/archive/bifrost/x86_64/gzip-1.4-1.tar.bz2  
run tar xvf gzip-1.4-1.tar.bz2 -C /out  
  
from wget AS bz  
run wget http://s.minos.io/archive/bifrost/x86_64/bzip2-bin-1.0.5-1.tar.gz  
run tar xvf bzip2-bin-1.0.5-1.tar.gz -C /out  
  
from wget AS xz  
run wget http://s.minos.io/archive/bifrost/x86_64/xz-5.0.3-1.tar.gz  
run tar xvf xz-5.0.3-1.tar.gz -C /out  
  
from scratch AS release  
copy \--from=upx /copy /bin/  
# copy --from=cp /bin/cp /bin/  
copy \--from=tar /out/bin /bin/  
copy \--from=gz /out/bin /bin/  
copy \--from=bz /out/bin /bin/  
copy \--from=xz /out/usr/bin /bin/  
entrypoint ["/bin/copy"]  
  
from alpine as dev-env  
copy \--from=release /bin/ /bin/  
entrypoint ["ash"]  
  
from release  

