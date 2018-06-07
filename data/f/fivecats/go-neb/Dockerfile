FROM golang  
  
RUN mkdir /data  
RUN go get github.com/constabulary/gb/...  
RUN git clone https://github.com/matrix-org/go-neb \  
&& cd go-neb \  
&& gb build github.com/matrix-org/go-neb  
  
ENV BIND_ADDRESS=:4050 DATABASE_TYPE=sqlite3 DATABASE_URL=/data/go-
neb.db?_busy_timeout=5000  
VOLUME /data  
EXPOSE 4050  
ENTRYPOINT ["/go/bin/go-neb"]  

