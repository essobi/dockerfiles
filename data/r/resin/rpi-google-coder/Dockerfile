FROM resin/rpi-raspbian  
MAINTAINER petrosagg@resin.io  
  
ENV NODE_JS_HOME /opt/node  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/node/bin  
  
RUN apt-get update  
RUN apt-get install -y -q git curl python make build-essential  
RUN curl http://nodejs.org/dist/v0.10.21/node-v0.10.21-linux-arm-pi.tar.gz |
tar xz && mv node-v0.10.21-linux-arm-pi /opt/node  
  
RUN git clone https://github.com/googlecreativelab/coder  
RUN cd /coder/coder-base && npm install  
RUN cd /coder/coder-apps && ./install_pi.sh /coder/coder-base || true  
  
VOLUME ["/coder/coder-base"]  
  
EXPOSE 8081  
WORKDIR /coder/coder-base  
CMD ["/opt/node/bin/node", "server"]

