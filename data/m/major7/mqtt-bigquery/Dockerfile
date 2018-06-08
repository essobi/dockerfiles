FROM alpine:3.5  
RUN apk add --no-cache ca-certificates && update-ca-certificates  
  
COPY dist/mqtt-bq /mqtt-bq  
  
ENV GOOGLE_APPLICATION_CREDENTIALS=/credentials/key.json  
  
CMD ["/mqtt-bq"]

