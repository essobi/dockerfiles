FROM fedora  
  
RUN curl https://packages.microsoft.com/config/rhel/7/mssql-server.repo >
/etc/yum.repos.d/mssql-server.repo  
RUN dnf install -y mssql-server sudo  
  
#LABEL RUN-INTERACTIVE /usr/bin/docker run -it -v
\${DATADIR}:/var/opt/mssql/data:rw,z -v \${LOGDIR}:/var/opt/mssql/log:rw,z -e
ACCEPT_EULA=\${ACCEPT_EULA} -e SA_PASSWORD=\${SA_PASSWORD} IMAGE /bin/bash  
LABEL RUN /usr/bin/docker run -d -t -v \${DATADIR}:/var/opt/mssql/data:rw,z -v
\${LOGDIR}:/var/opt/mssql/log:rw,z -e ACCEPT_EULA=\${ACCEPT_EULA} -e
SA_PASSWORD=\${SA_PASSWORD} IMAGE  
  
#ENV SA_PASSWORD  
#ENV ACCEPT_EULA  
VOLUME /var/opt/mssql/data  
VOLUME /var/opt/mssql/log  
EXPOSE 1433  
ADD start.sh /start.sh  
#RUN chmod a+x /start.sh  
CMD ["/start.sh"]  
  

