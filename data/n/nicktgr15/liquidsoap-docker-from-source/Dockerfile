FROM savonet/liquidsoap-deps  
  
USER opam  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/savonet/liquidsoap-full.git  
  
WORKDIR /tmp/liquidsoap-full  
  
RUN make init && make update  
  
RUN cp PACKAGES.default PACKAGES  
  
RUN ./bootstrap  
  
RUN eval $(opam config env) && ./configure && make clean && make  
  
USER root  
  
RUN make install  
  
USER opam  
  
RUN openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout /tmp/server.key
-out /tmp/server.crt -subj "/CN=localhost" -days 3650  
  
COPY my.liq /my.liq  

