# We're basing the image on ubuntu instead of python because we need to
install  
# Microsoft ODBC Driver for SQL Server, which only supports ubuntu (not
debian).  
FROM ubuntu:16.04  
# Install python3 and pip  
RUN apt-get update \  
&& apt-get install -y python3 python-pip \  
&& rm -rf /var/lib/apt/lists/*  
# Install Microsoft ODBC Driver for SQL Server  
RUN apt-get update \  
&& apt-get install -y apt-transport-https curl \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list \  
&& apt-get update \  
&& ACCEPT_EULA=Y apt-get install -y msodbcsql=13.0.1.0-1 mssql-
tools=14.0.2.0-1 unixodbc-dev-utf16 locales \  
&& ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd \  
&& ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp \  
&& locale-gen en_US.UTF-8 \  
&& rm -rf /var/lib/apt/lists/*  
# Install sandman2 and pyodbc  
RUN pip install sandman2 pyodbc  
  
# Copy start file  
COPY start.sh /start.sh  
  
# Configure the listening port  
ENV PORT 80  
EXPOSE 80  
# Set start command  
CMD ["/start.sh"]  

