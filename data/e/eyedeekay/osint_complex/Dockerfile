FROM alpine:edge  
RUN apk update && apk upgrade  
RUN apk add nmap nmap-scripts bash  
RUN adduser -g 'scan,,,,' -D -h /home/scan scan scan  
COPY nmap-vulners/vulners.nse /home/scan/.nmap/scripts/vulners.nse  
USER scan  
ENTRYPOINT [ "nmap", "-sV", "--script", "vulners" ]  

