FROM golang:1.8  
COPY . "/go/src/AgendaService"  
# ENV http_proxy="http://172.17.0.1:1080" \  
# https_proxy="http://172.17.0.1:1080"  
RUN go get -v AgendaService/server AgendaService/client && \  
go install AgendaService/server && go install AgendaService/client  
EXPOSE 8080  
VOLUME [ "/data" ]  
ENTRYPOINT [ "/go/src/AgendaService/docker-entry.sh" ]  

