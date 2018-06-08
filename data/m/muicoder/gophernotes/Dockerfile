FROM python:3.6  
ENV DEBIAN_FRONTEND=noninteractive  
  
SHELL ["bash", "-c"]  
  
# golang  
ARG GOLANG_VERSION=1.8.3  
ENV GOPATH=/go \  
GOROOT=/usr/local/go  
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin  
RUN mkdir -p $GOROOT $GOPATH/{src,bin,pkg} \  
&& curl -fsSL https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-
amd64.tar.gz -o pkg.tar.gz \  
&& tar -xf pkg.tar.gz --strip-components 1 -C $GOROOT && rm -fv pkg.tar.gz \  
&& chmod -R 777 $GOPATH  
  
WORKDIR $GOPATH  
  
# gophernotes  
RUN apt-get -qqy update && \  
apt-get -qqy install libzmq3-dev build-essential bash-completion vim && \  
INSTALL_PATH=/sbin \  
TINI_VERSION=0.14.0 \  
TINI_SHA=b2d2b6d7f570158ae5eccbad9b98b5e9f040f853 \  
GOSU_SHA=8068f973713558e750b5cbe74e2c5a40d6aeb631 \  
GOSU_VERSION=1.10 && \  
curl -fsSL
https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini-static-
amd64 \  
-o $INSTALL_PATH/tini ; echo "$TINI_SHA $INSTALL_PATH/tini" | sha1sum -c - && \  
curl -fsSL
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64 \  
-o $INSTALL_PATH/gosu ; echo "$GOSU_SHA $INSTALL_PATH/gosu" | sha1sum -c - && \  
chmod +x $INSTALL_PATH/* && \  
\  
curl -fsSL https://github.com/muicoder/gophernotes/raw/master/venv.sh \  
-o /etc/profile.d/venv.sh && \  
\  
go get golang.org/x/tools/cmd/goimports && \  
go get -tags zmq_4_x github.com/gopherds/gophernotes && \  
mkdir -pv ~/.local/share/jupyter/kernels/gophernotes && \  
mv -fv $GOPATH/src/github.com/gopherds/gophernotes/kernel/* \  
~/.local/share/jupyter/kernels/gophernotes && \  
mv -fv $GOPATH/bin/* $INSTALL_PATH && \  
\  
pip install -U pip setuptools \  
jupyter virtualenvwrapper && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/* /var/log/* /tmp/*
$GOPATH/{src,bin,pkg}/*  
  
VOLUME ["/go", "/python"]  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "-s", "--"]  
CMD ["jupyter-notebook", "--no-browser", "--allow-root"]  

