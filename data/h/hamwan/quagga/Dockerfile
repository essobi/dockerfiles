FROM alpine  
RUN apk add --no-cache quagga \  
supervisor  
ADD supervisord.conf /etc/supervisord.conf  
RUN touch /etc/quagga/zebra.conf && \  
touch /etc/quagga/ospfd.conf  
VOLUME /etc/quagga  
EXPOSE 2601 \  
2602 \  
2603 \  
2604 \  
2605 \  
2606  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  

