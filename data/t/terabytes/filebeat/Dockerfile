FROM golang:latest  
RUN cd /go/src && git clone https://github.com/elastic/beats.git && \  
cd beats/filebeat && go get && go build && mv filebeat /usr/bin/ && \  
rm -rf /go  
ADD . /opt/filebeat/  
ENTRYPOINT ["/opt/filebeat/docker-entrypoint.sh"]  
CMD ["/usr/bin/filebeat", "-c", "/opt/filebeat/filebeat.yml"]  

