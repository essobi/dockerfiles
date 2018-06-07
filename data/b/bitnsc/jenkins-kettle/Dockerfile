FROM jenkins  
MAINTAINER liling@bit.edu.cn  
  
USER root  
  
# Setup timezone  
RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Setup locale  
ENV LC_ALL C.UTF-8  
  
RUN apt-get update; apt-get -y upgrade; apt-get install -y lftp curl wget
dstat dnsutils rlwrap libaio-dev  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD oracle/*.deb /tmp/  
RUN dpkg -i /tmp/*.deb ; rm -f /tmp/*.deb  
ADD oracle/*.jar /usr/lib/oracle/12.1/client64/lib/  
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64  
ENV NLS_LANG "SIMPLIFIED CHINESE_CHINA.AL32UTF8"  
ADD oracle/ld_oracle.conf /etc/ld.so.conf.d/oracle.conf  
RUN ldconfig  
# Add profile  
ADD rlwrap.sh /etc/profile.d  
  
# Unpack Kettle  
ENV KETTLE_VERSION 5.4.0.1-130  
RUN cd /opt && wget -O pdi-ce-${KETTLE_VERSION}.zip
"https://sourceforge.net/projects/pentaho/files/Data%20Integration/5.4/pdi-
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
  
USER jenkins  

