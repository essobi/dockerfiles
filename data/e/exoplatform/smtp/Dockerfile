#FROM alpine:3.3  
FROM debian:8.0  
ARG POSTFIX_UID=1000  
RUN useradd -u ${POSTFIX_UID} -s /bin/false postfix && apt-get update && apt-
get install -y postfix rsyslog  
  
COPY entrypoint.sh /  
COPY rsyslog.conf /etc/  
  
RUN chmod u+x entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
EXPOSE 25  

