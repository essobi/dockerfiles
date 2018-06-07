FROM microsoft/mssql-server-linux:2017-latest  
  
ENV ACCEPT_EULA Y  
ENV SA_PASSWORD '<YourStrong!Passw0rd>'  
ENV MSSQL_PID Developer  
  
COPY entrypoint.sh /  
COPY mssql-setup.sh /  
RUN chmod +x /entrypoint.sh \  
&& chmod +x /mssql-setup.sh \  
&& mkdir /docker-entrypoint-initdb.d  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  
  

