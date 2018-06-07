FROM ubuntu  
  
ENV XMRIG_DIR /xmrig-cpu  
ENV XMRIG_BUILD_DIR $XMRIG_DIR/build  
ENV XMRIG_SRC_DIR $XMRIG_DIR/src  
  
RUN apt-get update && apt-get install -y curl git build-essential cmake
libuv1-dev libmicrohttpd-dev software-properties-common  
RUN add-apt-repository ppa:jonathonf/gcc-7.1 && apt-get update && apt-get
install -y gcc-7 g++-7  
RUN git clone https://github.com/xmrig/xmrig.git $XMRIG_DIR && cd $XMRIG_DIR
&& ls  
RUN echo "#ifndef __DONATE_H__" > $XMRIG_SRC_DIR/donate.h && echo "#define
__DONATE_H__" >> $XMRIG_SRC_DIR/donate.h && echo "constexpr const int
kDonateLevel = 0;" >> $XMRIG_SRC_DIR/donate.h && echo "#endif" >>
$XMRIG_SRC_DIR/donate.h  
RUN mkdir $XMRIG_BUILD_DIR && cd $XMRIG_BUILD_DIR && \  
cmake .. -DWITH_HTTPD=OFF -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7
&& make  
RUN mv $XMRIG_BUILD_DIR/xmrig /usr/bin/  
  
ENTRYPOINT ["xmrig"]  

