FROM golang:1.7.3-alpine  
  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
ENV CALENDAR_RESOURCE_REPOSITORY ${GOPATH}/src/github.com/henrytk/calendar-
resource  
RUN git clone https://github.com/henrytk/calendar-resource
${CALENDAR_RESOURCE_REPOSITORY} \--branch master  
RUN cd ${CALENDAR_RESOURCE_REPOSITORY} && \  
go build -o built-check ./cmd/check/  
RUN cd ${CALENDAR_RESOURCE_REPOSITORY} && \  
go build -o built-in ./cmd/in/  
RUN cd ${CALENDAR_RESOURCE_REPOSITORY} && \  
go build -o built-out ./cmd/out/  
  
RUN mkdir -p /opt/resource  
RUN mv ${CALENDAR_RESOURCE_REPOSITORY}/built-check /opt/resource/check  
RUN mv ${CALENDAR_RESOURCE_REPOSITORY}/built-in /opt/resource/in  
RUN mv ${CALENDAR_RESOURCE_REPOSITORY}/built-out /opt/resource/out  

