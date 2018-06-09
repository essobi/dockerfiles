FROM alpine:3.4  
LABEL Description="tinyproxy" \  
Vendor="ACME Products" \  
Version="1.0" \  
authors="Rodrigo de la Fuente <rodrigo@delafuente.email>, pancho horrillo
<pancho@pancho.name>"  
  
RUN apk --no-cache add tinyproxy  
ENTRYPOINT ["/usr/sbin/tinyproxy"]  
CMD ["-d"]  

