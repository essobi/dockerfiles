FROM graylog2/allinone  
MAINTAINER Ronald Rink <ronald.rink@d-fens.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# run graylog-server with debugger  
# RUN sed -i 's/\\(GRAYLOG_SERVER_JAVA_OPTS=".*\\)"/\1
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005"/'
/opt/graylog/embedded/cookbooks/graylog/templates/default/sv-graylog-server-
run.erb  
VOLUME /var/opt/graylog/data  
VOLUME /var/log/graylog  
VOLUME /opt/graylog/plugin  
  
# web interface  
EXPOSE 9000  
# gelf tcp  
EXPOSE 12201  
# gelf udp  
EXPOSE 12201/udp  
# gelf tcp  
EXPOSE 12202  
# gelf udp  
EXPOSE 12202/udp  
# rest api  
EXPOSE 12900  
# etcd  
EXPOSE 4001  
# syslog  
EXPOSE 514  
EXPOSE 514/udp  
  
CMD ["/opt/graylog/embedded/share/docker/my_init"]  

