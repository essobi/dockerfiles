FROM golang:1.6.1  
RUN go get github.com/tools/godep  
  
WORKDIR /go/src/github.com/wndhydrnt/mesos-task-exporter  
  
COPY . /go/src/github.com/wndhydrnt/mesos-task-exporter  
  
RUN godep restore && go get -d  
  
RUN go build  
  
ENV EXPORTER_ADDRESS :55555  
ENV EXPORTER_ENDPOINT /metrics  
ENV LOG_LEVEL info  
ENV MESOS_MASTERS http://localhost:5050  
ENV MESOS_MASTER_POLLINTERVAL 15s  
ENV MESOS_SLAVE_POLLINTERVAL 15s  
  
EXPOSE 55555  
CMD ["/go/src/github.com/wndhydrnt/mesos-task-exporter/entrypoint.sh"]  

