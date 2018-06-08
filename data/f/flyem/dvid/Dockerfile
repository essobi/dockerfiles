FROM ubuntu:12.04  
MAINTAINER Stephen Plaza <plazas@janelia.hhmi.org>  
  
# set environment variables  
ENV GOROOT /usr/local/go  
ENV GOPATH=$HOME/go  
ENV DVIDSRC=$GOPATH/src/github.com/janelia-flyem/dvid  
ENV BUILDEM_DIR $HOME/buildem  
ENV LD_LIBRARY_PATH $BUILDEM_DIR/lib:$LD_LIBRARY_PATH  
ENV PATH /usr/local/go/bin:$BUILDEM_DIR/bin:$PATH  
ENV DVIDDATA /var/dvid  
ENV CONSOLEVERSION 1.11.0  
ENV DVIDVERSION v0.8.1  
ADD ./config.toml /var/config.toml  
ADD ./configbucket.toml /var/configbucket.toml  
ADD ./dvid.sh /usr/local/bin/dvid.sh  
  
# install basic dependencies  
RUN apt-get -y update && apt-get install -y \  
git \  
make \  
g++ \  
cmake \  
wget \  
mercurial \  
zip  
  
# install go binary  
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz && tar
-C /usr/local -xzf go1.5.linux-amd64.tar.gz  
  
# download web console  
RUN wget https://github.com/janelia-flyem/dvid-
console/releases/download/v${CONSOLEVERSION}/dvid-
console-${CONSOLEVERSION}.tar.gz && tar -C /usr/local -xzf dvid-
console-${CONSOLEVERSION}.tar.gz  
  
# make dvid from git head  
RUN mkdir $HOME/go; mkdir -p $DVIDSRC; \  
cd $DVIDSRC; cd ..; \  
git clone https://github.com/janelia-flyem/dvid; \  
cd $DVIDSRC; git reset --hard be6fadf1d8ea284e84aa414228ba10ea3201efba; mkdir
build; cd build; \  
cmake -DDVID_BACKEND="basholeveldb;gbucket" -DBUILDEM_DIR=$BUILDEM_DIR ..; \  
make; cmake -D BUILDEM_DIR=$BUILDEM_DIR ..; \  
make dvid; \  
cd $GOPATH/src/google.golang.org/cloud; git reset --hard
8bc2457bef5a52c10b0001d481d441141095b130; go install; \  
cd $DVIDSRC/build; make dvid; \  
chmod +x /usr/local/bin/dvid.sh  
  
# no argument: launch dvid (creates new db in /var/dvid/db unless already
provided)  
# one argument: specify google bucket containing dvid instance  
# logs are written to /data/logs  
ENTRYPOINT ["/usr/local/bin/dvid.sh"]  
CMD [""]  
  
EXPOSE 8000  

