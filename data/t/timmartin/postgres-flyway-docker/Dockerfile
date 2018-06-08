FROM java:7  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && \  
apt-get install -y maven postgresql-9.4 wget --fix-missing  
  
WORKDIR /opt/flyway  
  
# Install Flyway  
RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/3.2.1/flyway-commandline-3.2.1.tar.gz && \  
tar --remove-files -xvzf flyway-commandline-3.2.1.tar.gz && \  
ln -s /opt/flyway/flyway-3.2.1/flyway /usr/local/bin/flyway  
  
ENV APP_ROOT="/app"  
USER_ROOT="/home/postgres" \  
APP_USER="postgres" \  
APP_GROUP="postgres" \  
PGDATA="/var/lib/pgdata/data" \  
PATH="$PATH:/usr/lib/postgresql/9.4/bin"  
RUN mkdir -p $PGDATA  
WORKDIR $APP_ROOT  

