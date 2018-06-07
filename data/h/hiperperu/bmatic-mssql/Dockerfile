FROM microsoft/mssql-server-linux:latest  
  
ENV ACCEPT_EULA Y  
ENV SA_PASSWORD bm4t1cMSSQL  
ENV DB_DATA_HOME /var/opt/mssql/data  
ENV DB_LOG_HOME /var/opt/mssql/log  
  
COPY build.sh /src/  
COPY load.sh /src/  
COPY dbBMatic /src/dbBMatic  
COPY dbBMaticSeguridad /src/dbBMaticSeguridad  
COPY dbBMatic_Central /src/dbBMatic_Central  
COPY dbBMaticDataMart /src/dbBMaticDataMart  
COPY dbChannel /src/dbChannel  
  
WORKDIR /src  
  
RUN ./build.sh  
RUN ./load.sh  
  
WORKDIR /  
RUN rm -rf /src  
  
ENTRYPOINT /opt/mssql/bin/sqlservr  

