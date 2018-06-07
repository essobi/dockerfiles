FROM alpine:latest  
  
LABEL maintainer="GeniusRabbitCo (Dmitry Ponomarev <demdxx@gmail.com>)"  
LABEL service.name=eventstream  
LABEL service.weight=1  
  
ENV ZONEINFO=/zoneinfo.zip  
  
COPY ./eventstream /  
COPY ./config.hcl /  
COPY ./zoneinfo.zip /  
  
CMD /eventstream --config=/config.hcl  

