FROM mysql:8  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
mkdir /opt/employees_db && \  
curl -L https://github.com/datacharmer/test_db/archive/master.zip >
/opt/employees_db/download.zip && \  
unzip /opt/employees_db/download.zip -d /opt/employees_db && rm
/opt/employees_db/download.zip  
  
COPY CreateDatabase.sh /docker-entrypoint-initdb.d/CreateDatabase.sh  
  
RUN chmod +x /docker-entrypoint-initdb.d/CreateDatabase.sh  
  
ENV MYSQL_DATABASE=employees  
ENV MYSQL_RANDOM_ROOT_PASSWORD=yes  
ENV MYSQL_USER=test_user  
ENV MYSQL_PASSWORD=test_password

