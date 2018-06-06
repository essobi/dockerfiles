FROM ubuntu:18.04  
RUN apt-get update \  
&& apt-get install -y rabbitmq-server \  
python3-pip \  
capnproto \  
libsnappy-dev \  
libgoogle-perftools-dev \  
libssl-dev \  
libsodium* \  
libsecp256k1-dev \  
pkg-config \  
git \  
curl \  
libcurl4 \  
sysstat \  
sudo \  
&& cd .. \  
&& rm -rf /var/lib/apt/lists \  
&& apt-get autoremove \  
&& apt-get clean \  
&& apt-get autoclean  
  
RUN pip3 install -U pip  
RUN pip3 install pysodium toml jsonschema secp256k1 protobuf requests ecdsa \  
jsonrpcclient[requests]==2.4.2 \  
py_solc==3.0.0 \  
simplejson==3.11.1 \  
pathlib==1.0.1 \  
pysha3>=1.0.2  
RUN git clone https://github.com/ethereum/pyethereum/  
WORKDIR /pyethereum  
RUN git checkout 3d5ec14032cc471f4dcfc7cc5c947294daf85fe0  
RUN python3 setup.py install  
RUN rm -r /pyethereum && rm -r ~/.cache/pip  
  
WORKDIR /  
  
COPY solc /usr/bin/  
RUN chmod +x /usr/bin/solc  
  
COPY libgmssl.so.1.0.0 /usr/local/lib/  
RUN ln -srf /usr/local/lib/libgmssl.so.1.0.0 /usr/local/lib/libgmssl.so  
RUN ldconfig  
  
# Link: https://denibertovic.com/posts/handling-permissions-with-docker-
volumes/  
COPY gosu /usr/bin/  
COPY entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/gosu  
RUN chmod +x /usr/bin/entrypoint.sh  
  
WORKDIR /opt/cita-run  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

