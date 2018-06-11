FROM sergeyzh/centos6-java  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
  
RUN wget -O /root/lfs.tar.gz http://www.moonlit-
software.com/logfaces/downloads/lfs.4.1.2.linux.x86-64.tar.gz  
RUN cd /root ; tar zxf /root/lfs.tar.gz  
  
VOLUME [ "/root/logFacesServer/conf" ]  
  
RUN ln -s /root/logFacesServer/bin/lfs /etc/init.d/lfs  
  
RUN sed -i '1 a JAVA_HOME=/usr/java64/current' /etc/init.d/lfs  
RUN sed -i '2 a APP_BIN=/root/logFacesServer/bin' /etc/init.d/lfs  
RUN sed -i 's/WRAPPER_CMD=\"\\./WRAPPER_CMD=\"\$\\{APP_BIN\\}/'
/etc/init.d/lfs  
RUN sed -i 's/WRAPPER_CONF=\"\\./WRAPPER_CONF=\"\$\\{APP_BIN\\}/'
/etc/init.d/lfs  
  
ENV JAVA_HOME /usr/java64/current  
ENV PATH $PATH:$JAVA_HOME/bin  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  
  
EXPOSE 8050 55200 1468 55201 514  

