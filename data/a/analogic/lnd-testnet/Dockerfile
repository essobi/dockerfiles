FROM golang:1.10  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
ENTRYPOINT ["/init"]  
  
# Expose mainnet ports (server, rpc)  
EXPOSE 8333 8334  
# Expose testnet ports (server, rpc)  
EXPOSE 18333 18334  
# Expose simnet ports (server, rpc)  
EXPOSE 18555 18556  
# Expose segnet ports (server, rpc)  
EXPOSE 28901 28902  
# Force Go to use the cgo based DNS resolver. This is required to ensure DNS  
# queries required to connect to linked containers succeed.  
ENV GODEBUG netdns=cgo  
  
# Install dep to manage vendor.  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN go get -u github.com/Masterminds/glide  
  
# ---------------------------------------------------------------------------  
# btcd  
# ---------------------------------------------------------------------------  
WORKDIR $GOPATH/src/github.com/roasbeef/btcd  
RUN git clone https://github.com/roasbeef/btcd .  
RUN glide install  
RUN go install . ./cmd/...  
  
RUN mkdir "/rpc" "/root/.btcd" "/root/.btcctl"  
RUN touch "/root/.btcd/btcd.conf"  
  
# Manually generate certificate and add all domains, it is needed to connect  
# "btcctl" and "lnd" to "btcd" over docker links.  
RUN "/go/bin/gencerts" \--host="*" \--directory="/rpc" \--force  
  
# Create a volume to house pregenerated RPC credentials. This will be  
# shared with any lnd, btcctl containers so they can securely query btcd's RPC  
# server.  
# You should NOT do this before certificate generation!  
# Otherwise manually generated certificate will be overriden with shared  
# mounted volume! For more info read dockerfile "VOLUME" documentation.  
VOLUME ["/rpc"]  
  
# ---------------------------------------------------------------------------  
# lnd  
# ---------------------------------------------------------------------------  
# Grab and install the latest version of lnd and all related dependencies.  
RUN git clone https://github.com/lightningnetwork/lnd
$GOPATH/src/github.com/lightningnetwork/lnd  
  
# Make lnd folder default.  
WORKDIR $GOPATH/src/github.com/lightningnetwork/lnd  
  
# Instll dependency and install/build lnd.  
RUN dep ensure  
RUN go install . ./cmd/...  
  
ADD rootfs /

