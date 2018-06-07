FROM alpine  
RUN apk add --update ca-certificates  
WORKDIR /app  
COPY bin/gis_directions /app/  
ENTRYPOINT ["./gis_directions"]  

