FROM python:3-alpine  
  
RUN apk add --no-cache autoconf automake libtool curl make g++ unzip  
  
COPY protobuf/ /usr/src/protobuf  
  
RUN cd /usr/src/protobuf \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr  
RUN cd /usr/src/protobuf \  
&& make  
RUN cd /usr/src/protobuf \  
&& make check  
RUN cd /usr/src/protobuf #\  
&& make install \  
RUN ldconfig  
RUN cd /usr/src/protobuf/python \  
&& python3.5 setup.py build \  
&& python3.5 setup.py test \  
&& python3.5 setup.py install  
  
CMD ["python3.5"]

