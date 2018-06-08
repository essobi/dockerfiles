FROM alpine  
  
RUN apk add --update \  
curl \  
build-base \  
bash  
  
RUN curl -L https://people.seas.harvard.edu/~apw/stress/stress-1.0.4.tar.gz >
stress-1.0.4.tar.gz && \  
tar xzvf stress-1.0.4.tar.gz && \  
cd stress-1.0.4 && ./configure && make && make install  
  
ENTRYPOINT ["stress"]  
  
# CMD "--cpu 8 --io 4 --vm 2 --vm-bytes 128M --timeout 10s"  

