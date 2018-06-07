FROM traxair/oracle-java7  
  
RUN apt-get update && apt-get install -y xinetd ldap-utils curl jq gettext  
  
ADD
https://www.apache.org/dist/directory/apacheds/dist/2.0.0-M19/apacheds-2.0.0-M19-amd64.deb
/tmp/installer.deb  
RUN dpkg -i /tmp/installer.deb  
RUN mkdir /templates && mkdir /ldifs  
  
COPY files/health_check.sh /root/health_check.sh  
COPY files/healthchk /etc/xinetd.d/healthchk  
COPY ldifs/* /ldifs/  
  
RUN echo 'healthchk 11001/tcp' >> /etc/services  
  
EXPOSE 10389 10636 11001  
COPY templates/* /templates/  
  
COPY scripts/* /root/  
  
RUN chmod +x /root/*.sh  
  
ENV DOMAIN_NAME="effedil" DOMAIN_SUFFIX="it" ACCESS_CONTROL_ENABLED="true"
ACTIVEMQ_ENABLED="true"  
#ENTRYPOINT ["/root/start.sh"]  
CMD ["/root/start.sh"]  
  

