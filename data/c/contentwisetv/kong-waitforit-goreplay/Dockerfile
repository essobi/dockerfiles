FROM golang AS waitforit  
RUN go get github.com/ContentWise/waitforit  
  
FROM kong:0.9.5  
ARG GOREPLAY_VERSION=0.16.1  
ENV MILLIS_BETWEEN_WAIT_RETRIES=2000  
ENV SECONDS_TO_WAIT=86400  
COPY run.sh /opt/  
  
RUN wget -q -O -
https://github.com/buger/goreplay/releases/download/v${GOREPLAY_VERSION}/gor_${GOREPLAY_VERSION}_x64.tar.gz
| tar -xz -C /usr/local/bin  
COPY \--from=waitforit /go/bin/waitforit /usr/local/bin/waitforit  
  
RUN mkdir /usr/local/kong/logs  
RUN touch /usr/local/kong/logs/access.log  
RUN touch /usr/local/kong/logs/error.log  
  
CMD ["/opt/run.sh"]

