FROM bitnsc/jetty-9  
MAINTAINER lilingv@gmail.com  
  
# Install packages  
RUN apt-get update; apt-get -y upgrade; apt-get install -y unzip  
  
# Unpack Kettle  
ENV KETTLE_VERSION 6.1.0.1-196  
RUN cd /opt && wget -O pdi-ce-${KETTLE_VERSION}.zip
"https://sourceforge.net/projects/pentaho/files/Data%20Integration/6.1/pdi-
ce-${KETTLE_VERSION}.zip/download" ; unzip pdi-ce-${KETTLE_VERSION} ; rm -f
pdi-ce-${KETTLE_VERSION}  
  
# Add JDBC Driver  
RUN ln -s /usr/lib/oracle/12.1/client64/lib/ojdbc6.jar /opt/data-
integration/lib/ ; ln -s /usr/lib/oracle/12.1/client64/lib/orai18n.jar
/opt/data-integration/lib/ ; ln -s /usr/lib/oracle/12.1/client64/lib/ucp.jar
/opt/data-integration/lib/  
  
RUN cd /tmp ; wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-5.1.39.tar.gz -O - | tar zxf - ; cp mysql*/*-bin.jar /opt/data-
integration/lib/ ; rm -rf mysql*  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

