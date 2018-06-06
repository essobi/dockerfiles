# Dockerfile for Hyperledger fabric-ca image.  
# If you need a peer node to run, please see the yeasy/hyperledger-peer image.  
# Workdir is set to $GOPATH/src/github.com/hyperledger/fabric-ca  
# More usage infomation, please see https://github.com/yeasy/docker-
hyperledger-fabric-ca.  
FROM golang:1.9  
LABEL maintainer "Baohua Yang <yeasy.github.com>"  
  
ENV BASE_VERSION 1.1.0  
# ca-server and ca-client will check the following env in order, to get the
home cfg path  
ENV FABRIC_CA_HOME /etc/hyperledger/fabric-ca-server  
ENV FABRIC_CA_SERVER_HOME /etc/hyperledger/fabric-ca-server  
ENV FABRIC_CA_CLIENT_HOME $HOME/.fabric-ca-client  
ENV CA_CFG_PATH /etc/hyperledger/fabric-ca  
  
# This is go simplify this Dockerfile  
ENV FABRIC_CA_ROOT $GOPATH/src/github.com/hyperledger/fabric-ca  
  
# Usually the binary will be installed into $GOPATH/bin, but we add local
build path, too  
ENV PATH=$FABRIC_CA_ROOT/bin:$PATH  
  
# fabric-ca-server will open service to '0.0.0.0:7054/api/v1/'  
EXPOSE 7054  
RUN mkdir -p $GOPATH/src/github.com/hyperledger \  
$FABRIC_CA_SERVER_HOME \  
$FABRIC_CA_CLIENT_HOME \  
$CA_CFG_PATH \  
/var/hyperledger/fabric-ca-server  
  
# Need libtool to provide the header file ltdl.h  
RUN apt-get update \  
&& apt-get install -y libtool unzip \  
&& rm -rf /var/cache/apt  
  
# clone and build ca  
RUN cd $GOPATH/src/github.com/hyperledger \  
&& git clone \--single-branch -b master --depth 1
https://github.com/hyperledger/fabric-ca \  
# This will install fabric-ca-server and fabric-ca-client into $GOPATH/bin/  
#&& go install -ldflags " -linkmode external -extldflags '-static -lpthread'"
github.com/hyperledger/fabric-ca/cmd/... \  
&& go install -ldflags "-X github.com/hyperledger/fabric-
ca/cmd.Version=$BASE_VERSION" github.com/hyperledger/fabric-ca/cmd/... \  
# Copy example ca and key files  
&& cp $FABRIC_CA_ROOT/images/fabric-ca/payload/*.pem $FABRIC_CA_HOME/  
  
VOLUME $FABRIC_CA_SERVER_HOME  
VOLUME $FABRIC_CA_CLIENT_HOME  
  
WORKDIR $FABRIC_CA_ROOT  
  
# if no config exists under $FABRIC_CA_HOME, will init fabric-ca-server-
config.yaml and fabric-ca-server.db  
CMD ["bash", "-c", "fabric-ca-server start -b admin:adminpw"]  
#CMD ["bash", "-c", "fabric-ca-server start --ca.certfile $FABRIC_CA_HOME/ca-
cert.pem --ca.keyfile $FABRIC_CA_HOME/ca-key.pem -b admin:adminpw -n test_ca"]  

