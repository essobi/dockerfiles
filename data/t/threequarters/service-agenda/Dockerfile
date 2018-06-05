FROM golang:1.8  
RUN mkdir -p /go/src/github.com/freakkid/service-agenda/  
WORKDIR /go/src/github.com/freakkid/service-agenda/  
COPY . .  
ENV SERVER_ADDR=agendad  
ENV PORT=8080  
WORKDIR /go/src/github.com/freakkid/service-agenda/cli  
RUN go-wrapper download && go build -o agenda && mv ./agenda /go/bin/  
  
WORKDIR /go/src/github.com/freakkid/service-agenda/service  
RUN go-wrapper download && go build -o agendad && mv ./agendad /go/bin/ && mv
../agenda.sh / && chmod +x /agenda.sh  
  
WORKDIR /  
ENTRYPOINT [ "./agenda.sh" ]  
CMD [ "agendad" ]  

