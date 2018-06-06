FROM nickball/jmeter-base:2.13  
ENV SSH_PORT 22  
ENV JMETER_PORT 20000  
ENV RMI_PORT 1099  
EXPOSE ${SSH_PORT}  
  
WORKDIR ${JMETER_HOME}  
  
CMD ["/opt/run.sh"]  
  
RUN apk update && \  
apk add bash openssh && \  
sed -i "s/#Port 22/Port ${SSH_PORT}/g" /etc/ssh/sshd_config && \  
rm -rf /var/cache/apk/*  
  
COPY run.sh /opt/run.sh  
RUN chmod +x /opt/run.sh  

