FROM ubuntu:14.04  
MAINTAINER Reinhard Brandstaedter, reinhard.brandstaedter@dynatrace.com  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists  
  
RUN echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf  
RUN echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf  
RUN echo "net.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf  
  
RUN cd /tmp && wget --progress=bar:force --no-check-certificate --no-cookies
--header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz
&& cd /opt && tar zxvf /tmp/jdk-8u45-linux-x64.tar.gz  
  
RUN cd /tmp && wget --progress=bar:force
http://downloads.dynatracesaas.com/freetrial/dynatrace-linux-x64.jar  
  
WORKDIR /opt  
RUN echo 'Y' | /opt/jdk1.8.0_45/bin/java -jar /tmp/dynatrace-linux-x64.jar  
  
RUN rm /tmp/dynatrace*.jar  
RUN rm /tmp/jdk*  
RUN rm -rf /opt/jdk*  
  
WORKDIR /opt/dynatrace-6.2/  
  
# update host agent config - serverhost, agent name  
RUN sed -i 's/-restartonfailure/-restartonfailure\n-memory\ndemo/g'
"/opt/dynatrace-6.2/dtserver.ini"  
RUN sed -i 's/-restartonfailure/-restartonfailure\n-memory\ndemo/g'
"/opt/dynatrace-6.2/dtfrontendserver.ini"  
  
RUN mkdir /opt/dynatrace-6.2/server/deployment/  
  
WORKDIR /opt/dynatrace-6.2/server/deployment/  
RUN wget --progress=bar:force https://github.com/dynaTrace/Dynatrace-hybris-
eCommerce-Fastpack/releases/download/v2.5/hybris-fastpack-2.5.dtp  
  
#COPY dtlicense.key /opt/dynatrace-6.2/server/conf/dtlicense.key  
#COPY server.config.xml /opt/dynatrace-6.2/server/conf/server.config.xml  
WORKDIR /opt/dynatrace-6.2/  
# RUN /opt/dynatrace-6.2/init.d/dynaTraceServer start  
#RUN /opt/dynatrace-6.2/dtserver -bg  
#RUN /opt/dynatrace-6.2/dtfrontendserver -bg  
RUN echo "#!/bin/bash" >> /opt/entrypoint.sh  
RUN echo "rm /var/run/dt*server.pid" >> /opt/entrypoint.sh  
RUN echo "/opt/dynatrace-6.2/init.d/dynaTraceCollector start" >>
/opt/entrypoint.sh  
RUN echo "/opt/dynatrace-6.2/init.d/dynaTraceServer start" >>
/opt/entrypoint.sh  
RUN echo 'exec "$@"' >> /opt/entrypoint.sh  
  
RUN chmod 755 /opt/entrypoint.sh  
  
ENTRYPOINT ["/opt/entrypoint.sh"]  
  
EXPOSE 2021  
EXPOSE 2030  
EXPOSE 2031  
EXPOSE 6699  
EXPOSE 8020  
EXPOSE 8021  
EXPOSE 8033  
EXPOSE 8091  
EXPOSE 8094  
EXPOSE 8079  
EXPOSE 9911  
EXPOSE 9912  
EXPOSE 9998  

