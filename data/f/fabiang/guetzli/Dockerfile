FROM ubuntu:latest  
  
WORKDIR /guetzli  
  
RUN apt-get update && \  
apt-get install -y libpng-dev libgflags-dev wget make g++  
  
RUN wget --no-check-certificate
https://github.com/google/guetzli/archive/v1.0.tar.gz && \  
tar -zxvf v1.0.tar.gz && \  
rm v1.0.tar.gz && \  
cd guetzli-1.0 && \  
make && \  
cp bin/Release/guetzli /usr/bin/guetzli && \  
cd .. && \  
rm -rf guetzli-1.0  
  
RUN apt-get remove -y libpng-dev libgflags-dev wget make g++  
  
VOLUME ["/guetzli"]  
ENTRYPOINT ["/usr/bin/guetzli"]  

