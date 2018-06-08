FROM mariadb:10.1  
MAINTAINER Michael Neßlinger <Michael.Nesslinger@gmx.de>  
  
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD:-verysecret}  
ENV MYSQL_DATABASE=${MYSQL_DATABASE:-flyway}  
ENV MYSQL_USER=${MYSQL_USER:-user}  
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD:-secret}  
  
ENV FLYWAY_VERSION='4.0.3'  
ENV FLYWAY_POPULATE_DATABASE=${FLYWAY_POPULATE_DATABASE:-false}  
ENV FLYWAY_DATABASE=${FLYWAY_DATABASE:-${MYSQL_DATABASE}}  
ENV FLYWAY_DATABASE_VERSION=${FLYWAY_DATABASE_VERSION:-1_0_2}  
ENV FLYWAY_PATH=/opt/flyway/flyway-${FLYWAY_VERSION}  
  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget  
  
RUN wget -O /tmp/flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz
https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/4.0.3/flyway-
commandline-${FLYWAY_VERSION}-linux-x64.tar.gz  
RUN mkdir -p /opt/flyway  
RUN tar -xzf /tmp/flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz -C
/opt/flyway  
  
ADD ./configuration/flyway/config/flyway.conf ${FLYWAY_PATH}/conf/flyway.conf  
  
RUN sed -i "s/^flyway.user$/flyway.user=$MYSQL_USER/g"
${FLYWAY_PATH}/conf/flyway.conf  
RUN sed -i "s/^flyway.password$/flyway.password=$MYSQL_PASSWORD/g"
${FLYWAY_PATH}/conf/flyway.conf  
RUN sed -i "s/^flyway.schemas$/flyway.schemas=$FLYWAY_DATABASE/g"
${FLYWAY_PATH}/conf/flyway.conf  
  
RUN ln -s ${FLYWAY_PATH}/sql /data  
RUN ln -s /etc/mysql/conf.d /config  
  
ADD ./configuration/flyway/sql/V1_0_0__Initial_structure.sql
${FLYWAY_PATH}/sql/V1_0_0__Initial_structure.sql  
ADD ./configuration/flyway/sql/V1_0_1__Add_color_column.sql
${FLYWAY_PATH}/sql/V1_0_1__Add_color_column.sql  
ADD ./configuration/flyway/sql/V1_0_2__Populate_table.sql
${FLYWAY_PATH}/sql/V1_0_2__Populate_table.sql  
ADD ./configuration/flyway/sql/R__Create_View_Blue_Cars.sql
${FLYWAY_PATH}/sql/R__Create_view_Blue_Cars.sql  
  
ADD ./configuration/mariadb/startup.sh /opt/flyway/startup.sh  
RUN chmod a+x /opt/flyway/startup.sh  
  
ENTRYPOINT ["/opt/flyway/startup.sh"]  
  
CMD ["mysqld"]

