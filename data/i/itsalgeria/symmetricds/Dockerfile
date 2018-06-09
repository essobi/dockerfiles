FROM anapsix/alpine-java:jre7  
ENV VERSION 3.9.2  
RUN adduser -D symmetricds  
ADD symmetric-server-3.9.2.zip symmetric-server-3.9.2.zip  
RUN unzip -q symmetric-server-3.9.2.zip -d /opt/  
RUN mv /opt/symmetric-server-3.9.2 /opt/symmetric  
RUN chown -R symmetricds /opt/symmetric  
RUN chmod -R 777 /opt/symmetric  
RUN rm symmetric-server-3.9.2.zip  
  
VOLUME /opt/symmetric/logs  
VOLUME /opt/symmetric/tmp  
VOLUME /opt/symmetric/engines  
  
USER symmetricds  
  
ENTRYPOINT ["/opt/symmetric/bin/sym"]  
  
EXPOSE 31415  
EXPOSE 31416  

