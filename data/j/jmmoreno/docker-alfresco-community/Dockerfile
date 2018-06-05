FROM centos:7  
MAINTAINER Jose Manuel Moreno Gavira <josem.moreno.gavira@gmail.com>  
  
# alfresco prerequisites  
RUN yum -y update  
RUN yum -y install fontconfig libSM libICE libXrender libXext cups-libs libGLU
cairo-devel libgl1-mesa-glx  
  
# copy java to /opt/ and extract it  
COPY files/tars/jdk-8u131-linux-x64.tar.gz-part-* /opt/  
RUN cat /opt/jdk-8u131-linux-x64.tar.gz-part-* >
/opt/jdk-8u131-linux-x64.tar.gz  
RUN tar -zxvf /opt/jdk-8u131-linux-x64.tar.gz -C /opt/  
RUN rm /opt/jdk-8u131-linux-x64.tar.gz*  
  
# actually we have a folder /opt/jdk1.8.0_131  
# config java pointing to JRE with environment variables  
ENV JAVA_HOME /opt/jdk1.8.0_131  
ENV JRE_HOME /opt/jdk1.8.0_131/jre  
ENV PATH PATH:$PATH:/opt/jdk1.8.0_131/bin:/opt/jdk1.8.0_131/jre/bin  
  
# copy alfresco base installation  
COPY files/tars/alfresco-community.tar.gz-part-* /opt/  
RUN cat /opt/alfresco-community.tar.gz-part-* > /opt/alfresco-community.tar.gz  
RUN tar -zxvf /opt/alfresco-community.tar.gz -C /opt/  
RUN rm /opt/alfresco-community.tar.gz*  
  
# actually we have a folder /opt/alfresco-community  
# forward logs from tomcat docker log collector  
RUN ln -sf /dev/stdout /opt/alfresco-community/tomcat/logs/catalina.out  
  
COPY files/encodepass.py /  
COPY files/changepass.sh /  
RUN chmod +x /encodepass.py && chmod +x /changepass.sh  
#RUN /bin/bash /changepass.sh  
ENV PASSWORD_RESTARTED 0  
COPY files/replacevars.sh /  
RUN chmod +x /replacevars.sh  
COPY files/entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# start alfresco  
ENTRYPOINT ["/entrypoint.sh"]

