FROM sergeyzh/centos6-java:jdk8  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
RUN /usr/sbin/useradd tomcat  
  
ENV TOMCAT_VER 8.0.43  
ENV TOMCAT_BIN apache-tomcat-${TOMCAT_VER}.tar.gz  
  
ENV WRAPPER_VER 3.5.26  
ENV WRAPPER_URL
http://wrapper.tanukisoftware.com/download/${WRAPPER_VER}/wrapper-
linux-x86-64-${WRAPPER_VER}.tar.gz  
  
RUN wget -O /home/tomcat/${TOMCAT_BIN}
https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VER}/bin/${TOMCAT_BIN}
&& \  
cd /home/tomcat && tar -xzf ${TOMCAT_BIN} && mv apache-tomcat-${TOMCAT_VER}
apache-tomcat-current && rm -rf apache-tomcat-current/webapps/* && \  
rm /home/tomcat/${TOMCAT_BIN}  
  
ADD wrapper.sed /  
  
RUN wget -O /home/tomcat/wrapper-linux-x86-64-${WRAPPER_VER}.tar.gz
${WRAPPER_URL} && cd /home/tomcat && \  
tar -xzf wrapper-linux-x86-64-${WRAPPER_VER}.tar.gz && \  
mv wrapper-linux-x86-64-${WRAPPER_VER} wrapper && \  
mv wrapper/bin/wrapper apache-tomcat-current/bin/ && \  
mv wrapper/conf/wrapper.conf apache-tomcat-current/conf/ && \  
mv wrapper/lib/libwrapper.so apache-tomcat-current/lib/ && \  
mv wrapper/lib/wrapper.jar apache-tomcat-current/lib/ && \  
sed -f /wrapper.sed < wrapper/src/bin/sh.script.in > /etc/init.d/tomcat && \  
chmod a+x /etc/init.d/tomcat && \  
rm /wrapper.sed && \  
rm -rf wrapper && \  
rm wrapper-linux-x86-64-${WRAPPER_VER}.tar.gz  
  
# Adding cacerts file from current Java disto to "conf" directory of Tomcat  
RUN cp /usr/java64/current/jre/lib/security/cacerts /home/tomcat/apache-
tomcat-current/conf/truststore  
  
ADD wrapper /home/tomcat/wrapper/  
ADD xslt /home/tomcat/xslt/  
ADD cacerts /home/tomcat/cacerts/  
  
ADD apply.sh /  
# Apply additional transformations for configs  
RUN bash -c ". /apply.sh"  
  
# Apply additional transformations to children images  
ONBUILD ADD wrapper /home/tomcat/wrapper/  
ONBUILD ADD xslt /home/tomcat/xslt/  
ONBUILD ADD cacerts /home/tomcat/cacerts/  
ONBUILD RUN bash -c ". /apply.sh"  
  
RUN chown -R tomcat:tomcat /home/tomcat && chmod -R a+rwX /home/tomcat &&
mkdir -p /root/prerun  
  
ADD run-tomcat.sh /  
  
CMD /run-tomcat.sh  
  
EXPOSE 8080  

