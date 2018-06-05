FROM ubuntu:14.04  
MAINTAINER tinoue  
  
# software-properties-common for add-apt-repository  
RUN apt-get update && apt-get install -y software-properties-common build-
essential git liblua5.1-0 liblua5.1-0-dev libprotobuf-dev libsqlite3-dev
protobuf-compiler shapelib libshp-dev  
  
RUN add-apt-repository ppa:ostogvin/tjo-develop && apt-get update && apt-get
install -y libboost1.58-all-dev  
  
RUN git clone https://github.com/rpavlik/luabind.git  
# The following line might not be necessary for you,  
# but I needed it to make sure that liblua was in /usr/lib:  
RUN ln -s /usr/lib/x86_64-linux-gnu/liblua5.1.so /usr/lib/  
RUN cd luabind && bjam install  
RUN ln -s /usr/local/lib/libluabindd.so /usr/local/lib/libluabind.so  
RUN sudo ldconfig  
  
CMD make

