FROM ubuntu:latest  
  
ARG PASSPHRASE=""  
ENV PASSPHRASE $PASSPHRASE  
  
WORKDIR /opt  
  
ADD shell2http .  
ADD generate.sh .  
ADD http.sh .  
  
RUN apt-get update && apt-get install putty-tools -y && chmod 755
/opt/shell2http /opt/generate.sh /opt/http.sh  
  
CMD /opt/http.sh  

