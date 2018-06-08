FROM alpine:latest  
  
# version of Radicale (e.g. 2.0.0)  
ARG VERSION=master  
  
# install dependencies  
RUN apk add --no-cache \  
python3 \  
python3-dev \  
build-base \  
libffi-dev \  
apache2-utils \  
ca-certificates \  
openssl && \  
python3 -m pip install passlib bcrypt && \  
apk del \  
python3-dev \  
build-base \  
libffi-dev  
  
# install Radicale  
RUN wget --quiet https://github.com/Kozea/Radicale/archive/${VERSION}.tar.gz \  
\--output-document=radicale.tar.gz && \  
tar xzf radicale.tar.gz && \  
python3 -m pip install ./Radicale-${VERSION} && \  
rm -r radicale.tar.gz Radicale-${VERSION}  
  
# single volume for Radicale persistent data  
VOLUME /radicale  
# mount using -v radicale:/radicale docker or -v /path/to:/radicale  
# tcp port for radicale  
EXPOSE 5232  
# publish on host interface with -p 5232:5232 or --network=host  
# set config environment variable  
ENV RADICALE_CONFIG /radicale/config  
  
# run Radicale (configure with args or provide a config file in
/radicale/config)  
CMD ["radicale", "--hosts", "0.0.0.0:5232", "--storage-filesystem-folder",
"/radicale/collections"]  

