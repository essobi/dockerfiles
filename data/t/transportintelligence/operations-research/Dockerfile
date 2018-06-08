FROM transportintelligence/operations-research:scip  
MAINTAINER Denis Arnaud <denis.arnaud_github at m4x dot org>  
LABEL version="0.1"  
  
# Environment  
ENV HOME /root  
ENV GOR_URL https://github.com/google/or-tools/archive  
ENV GOR_DIR /opt/google-or  
ENV GOR_VER 6.7.1  
ENV GOR_TAR v$GOR_VER.tar.gz  
  
# Update the system  
RUN apt -y update  
  
# Google OR  
RUN mkdir -p $GOR_DIR && cd $GOR_DIR && wget "$GOR_URL/$GOR_TAR"  
RUN cd $GOR_DIR && tar zxf $GOR_TAR  
RUN mkdir -p $GOR_DIR/or-tools-$GOR_VER/build && cd $GOR_DIR/or-
tools-$GOR_VER/build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON .. && make -j4
all install  
  
# Cleaning  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

