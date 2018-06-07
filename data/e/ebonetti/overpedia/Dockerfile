FROM postgres:latest  
  
# gcc for cgo and petsc, python for petsc, 7z for overpedia  
RUN set -eux; \  
apt-get update && apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
python \  
make \  
p7zip-full \  
curl \  
ca-certificates \  
git \  
pkg-config; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*;  
  
#install latest petsc  
ENV PETSC_DOWNLOAD_URL http://ftp.mcs.anl.gov/pub/petsc/petsc-lite.tar.gz  
ENV PETSC_ARCH arch-linux2-c-opt  
ENV PETSC_DIR /usr/local/petsc  
ENV PETSC_LIB $PETSC_DIR/$PETSC_ARCH/lib/  
ENV LD_LIBRARY_PATH $PETSC_LIB:$LD_LIBRARY_PATH  
RUN set -eux; \  
cd $PETSC_DIR/..; \  
curl -fsSL "$PETSC_DOWNLOAD_URL" -o petsc.tar.gz; \  
tar -xzf petsc.tar.gz; \  
rm petsc.tar.gz; \  
mv petsc* petsc; \  
cd $PETSC_DIR; \  
./configure --with-cc=gcc --with-cxx=0 --with-fc=0 --with-debugging=0 \  
# Optimization: if compiled somewhere, may not work elsewhere.  
# COPTFLAGS='-O3 -march=native -mtune=native' \  
\--download-mpich --download-f2cblaslapack; \  
make all test; \  
rm -rf /tmp/* /var/tmp/*;  
  
#install latest golang  
ENV GO_DIR /usr/local/go  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$GO_DIR/bin:$PATH  
RUN set -eux; \  
cd $GO_DIR/..; \  
V=10; \  
while curl --output /dev/null --silent --head --fail
"https://dl.google.com/go/go1.$V.linux-amd64.tar.gz"; do \  
GO_DOWNLOAD_URL="https://dl.google.com/go/go1.$V.linux-amd64.tar.gz"; \  
V=$((V+1)); \  
done; \  
V=$((V-1)); \  
v=1; \  
while curl --output /dev/null --silent --head --fail
"https://dl.google.com/go/go1.$V.$v.linux-amd64.tar.gz"; do \  
GO_DOWNLOAD_URL="https://dl.google.com/go/go1.$V.$v.linux-amd64.tar.gz"; \  
v=$((v+1)); \  
done; \  
curl -fsSL "$GO_DOWNLOAD_URL" -o go.tar.gz; \  
tar -xzf go.tar.gz; \  
rm go.tar.gz; \  
mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"; \  
go version;  
  
#install and compile overpedia  
ENV PROJECT github.com/ebonetti/overpedia  
ADD . $GOPATH/src/$PROJECT  
RUN set -eux; \  
cd /; \  
echo "#!/usr/bin/env bash\n\  
set -e;\n\  
\n\  
#Fork exec the postgres docker-entrypoint with postgres as command \n\  
postgres-entrypoint() {\n\  
set -- postgres\n\  
$(cat docker-entrypoint.sh)\n\  
}; postgres-entrypoint > /dev/null 2>&1 &\n\  
\n\  
mkdir -p /data/csv;\n\  
chown -R \$(stat -c '%u:%g' /data) /data;\n\  
exec \"\$@\"" > docker-entrypoint.sh; \  
go get $PROJECT/...;  
  
WORKDIR /data  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["refresh"]

