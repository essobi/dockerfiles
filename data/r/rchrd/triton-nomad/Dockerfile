FROM golang:1.5  
RUN mkdir -p /go/src/github.com/hashicorp && \  
cd /go/src/github.com/hashicorp && \  
git clone -b triton --single-branch https://github.com/rchrd/nomad.git && \  
cd nomad && \  
make bootstrap && \  
make dev  
  
COPY files/nomad.d/* /etc/nomad.d/  
COPY files/run.sh /run.sh  
RUN chmod u+x /run.sh  
  
CMD ["/run.sh"]  

