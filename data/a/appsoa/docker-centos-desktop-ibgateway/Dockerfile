#  
#  
FROM appsoa/docker-centos-desktop-vnc:latest  
  
USER root  
ENV INSTALL4J_JAVA_HOME /usr/java/jdk1.8.0_60  
COPY src/bin /bin  
COPY src/home /home  
COPY src/opt /opt  
  
ADD https://storage.googleapis.com/algolab-container-
resources/ibgateway.jars.tar /tmp/  
RUN tar -xvzf /tmp/ibgateway.jars.tar -C /home/user/Jts/ibgateway/962  
  
RUN yum -y install nc && \  
chmod +x /etc/xdg/xfce4/xinitrc && \  
# chmod 0 /usr/bin/xfce4-panel && \  
chown -R user:wheel /home/user /opt/IBController  
  
EXPOSE 4100 5901 4440  
# ENTRYPOINT ["/bin/ibgateway-settings.sh"]  
COPY src/entrypoint.sh /  
COPY src/entrypoint.d/* /entrypoint.d/  
ONBUILD COPY src/entrypoint.d/* /entrypoint.d/  
  
USER user  
ENTRYPOINT ["/entrypoint.sh"]

