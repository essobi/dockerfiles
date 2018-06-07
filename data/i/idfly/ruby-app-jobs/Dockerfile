FROM idfly/ruby-app  
  
ENV GOPATH=/root/go  
ENV PATH=/usr/local/bin:/usr/bin:/usr/sbin:/sbin/:/bin  
  
RUN apt-get update -qq && apt-get -y install golang  
RUN useradd --home / -M --system --shell /sbin/nologin jobber_client  
  
RUN go get github.com/dshearer/jobber  
RUN make -C /root/go/src/github.com/dshearer/jobber  
  
ENTRYPOINT /root/go/bin/jobberd start  

