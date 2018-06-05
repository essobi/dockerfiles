FROM alpine:3.6  
RUN apk update && apk upgrade && \  
apk add --no-cache \  
bash \  
tini \  
git \  
libzmq \  
zeromq \  
python3 \  
py3-netifaces \  
py3-zmq  
  
RUN cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s pip3 pip \  
&& ln -s python3-config python-config  
  
RUN pip3 install git+https://github.com/uniflex/uniflex@master  
  
EXPOSE 8989 8990  
ENTRYPOINT ["/sbin/tini", "-v", "--"]  
CMD ["uniflex-broker"]  

