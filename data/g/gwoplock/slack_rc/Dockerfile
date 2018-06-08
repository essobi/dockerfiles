  
FROM alpine:edge  
  
#install base packages  
RUN apk add --update --no-cache build-base curl-dev gcc musl-dev make boost-
dev git cmake asio-dev asio  
  
#move asio to the right place  
RUN cp -r usr/include/asio/ usr/include/boost/asio/  
  
#get the beast lib  
RUN git clone https://github.com/boostorg/beast.git && cd beast && cp -R
include /usr/local/ && cd ..  
  
#get cpp-netlib  
RUN wget http://downloads.cpp-netlib.org/0.12.0/cpp-
netlib-0.12.0-final.tar.bz2 && \  
tar -xf cpp-netlib-0.12.0-final.tar.bz2 && \  
cd cpp-netlib-0.12.0-final && cp -R boost /usr/local/include && cd ..  
  
#add src files  
ADD src/ SlackRC/src/  
ADD CMakeLists.txt SlackRC  
  
#build  
RUN cd SlackRC && mkdir Build && cd Build && cmake .. && make  
  
#expose IRC server  
EXPOSE 6667  
CMD ["SlackRC/Build/SlackRC"]  
  

