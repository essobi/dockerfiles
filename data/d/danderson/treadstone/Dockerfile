FROM alpine:edge  
  
ENV TREADSTONE_VPN_CONFIG="/openvpn.conf" TREADSTONE_VPN_ARGS=""
TREADSTONE_EXPOSE_PORTS=""  
COPY . /tmp/treadstone  
RUN /tmp/treadstone/build.sh  
ENTRYPOINT /treadstone/run.sh  

