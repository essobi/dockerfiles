FROM crystallang/crystal  
  
COPY ./clock.cr /tmp  
RUN crystal build -o /usr/bin/clock --release --single-module /tmp/clock.cr  
WORKDIR /  
ONBUILD COPY ./alerm /etc/alerm  
ENTRYPOINT ["clock"]  
CMD ["/etc/alerm"]  

