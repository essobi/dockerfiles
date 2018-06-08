FROM centos:7  
RUN yum -y update  
  
RUN yum install -y java-1.8.0-openjdk  
  
RUN yum install -y file openssl-devel initscripts sudo  
  
ENV PREFIX=/opt/firebird  
ENV DBPATH=/databases  
  
RUN bash -c "mkdir /databases"  
  
COPY ./scripts/install_fb25_hqbird_server_2017r2.sh .  
RUN chmod a+x install_fb25_hqbird_server_2017r2.sh  
RUN bash -c "./install_fb25_hqbird_server_2017r2.sh"  
COPY ./config/firebird/conf/firebird.conf ${PREFIX}  
COPY ./config/firebird/UDF ${PREFIX}/UDF  
RUN bash -c "echo \"process\" | ${PREFIX}/bin/changeMultiConnectMode.sh"  
  
EXPOSE 3050/tcp  
EXPOSE 8082/tcp  
EXPOSE 8765/tcp  
  
VOLUME ["/databases", "/opt/firebird"]  
  
RUN yum clean all  
RUN bash -c "rm -rf /var/cache/yum"  
  
COPY config/hqbird/conf /opt/hqbird/conf  
RUN chmod a+w /opt/hqbird/conf/access.properties  
  
COPY ./scripts/docker-entrypoint.sh .  
RUN chmod 777 /docker-entrypoint.sh  
  
COPY run.sh .  
RUN chmod a+x run.sh  
  
ENTRYPOINT /docker-entrypoint.sh /run.sh  

