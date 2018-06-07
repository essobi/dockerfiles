FROM qcifengineering/redbox:latest  
WORKDIR /opt/redbox  
RUN yum install -y tzdata && cp /usr/share/zoneinfo/Australia/NSW
/etc/localtime  
RUN yum install -y less cron vim  
COPY institutional-build /opt/redbox  
RUN chmod +x /opt/redbox/server/*.sh  
WORKDIR /opt/redbox/server  

