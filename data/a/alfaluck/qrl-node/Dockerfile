FROM ubuntu  
  
MAINTAINER alfaluck <alfaluck@gmail.com>  
  
COPY ./node /qrl-node  
  
WORKDIR /qrl-node  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
swig3.0 cmake pkg-config \  
build-essential libboost-random-dev libssl-dev libffi-dev \  
python3-dev python3-pip python3-setuptools \  
telnet \  
&& pip3 install -U pip setuptools \  
&& pip3 install -r requirements.txt \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& sed -i "s/TCP4ServerEndpoint(reactor, 8888,
interface='127.0.0.1')/TCP4ServerEndpoint(reactor, 8888)/" /qrl-
node/qrl/webwallet.py  
  
EXPOSE 8080 8888 9000  
  
CMD python3 start_qrl.py

