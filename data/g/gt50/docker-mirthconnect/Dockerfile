FROM centos:7  
ENV MIRTH_CONNECT_VERSION 3.5.2.b204  
  
RUN yum update -y  
RUN yum install -y wget  
RUN wget http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-
release-7-11.noarch.rpm && rpm -ihv epel-release-7-11.noarch.rpm \  
&& rm -f epel-release-7-11.noarch.rpm  
RUN yum install -y monit htop  
  
WORKDIR /opt/mirthconnect  
  
#RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" \  
# "http://download.oracle.com/otn-
pub/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/jre-9.0.4_linux-x64_bin.rpm"
\  
# && yum install -y jre-9.0.4_linux-x64_bin.rpm \  
# && rm -f jre-9.0.4_linux-x64_bin.rpm  
RUN yum install -y java-1.8.0-openjdk  
  
RUN wget
http://downloads.mirthcorp.com/connect/$MIRTH_CONNECT_VERSION/mirthconnect-$MIRTH_CONNECT_VERSION-
linux.rpm \  
&& yum install -y mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm \  
&& sed -i 's/8080/80/g' /opt/mirthconnect/conf/mirth.properties \  
&& sed -i 's/8443/443/g' /opt/mirthconnect/conf/mirth.properties \  
&& sed -i 's/-Xmx256m/-Xmx1024m/g' /opt/mirthconnect/mcserver.vmoptions \  
&& sed -i 's/-Xmx256m/-Xmx1024m/g' /opt/mirthconnect/mcservice.vmoptions \  
&& sed -i '/start com.mirth.connect.server.launcher.MirthLauncher/a\echo $! >
/var/run/mcservice.pid' mcservice \  
&& sed -i '/com.install4j.runtime.launcher.Launcher stop/a\rm
/var/run/mcservice.pid' mcservice \  
&& rm -f mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm  
  
RUN sed -i "\$acheck process mcservice with pidfile /var/run/mcservice.pid"
/etc/monitrc \  
&& sed -i "\$a start program = \"/opt/mirthconnect/mcservice start\" with
timeout 60 seconds" /etc/monitrc \  
&& sed -i "\$a stop program = \"/opt/mirthconnect/mcservice stop\""
/etc/monitrc \  
&& sed -i "\$a if cpu > 60% for 2 cycles then alert" /etc/monitrc \  
&& sed -i "\$a if cpu > 90% for 5 cycles then restart" /etc/monitrc  
  
EXPOSE 80 443  
CMD /opt/mirthconnect/mcservice restart && monit && tail -F
/opt/mirthconnect/logs/mirth.log  

