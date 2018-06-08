FROM pulsepointinc/centos7-java8:latest  
  
ENV KM_RELEASE=1.3.3.15  
RUN \  
rpm --rebuilddb && \  
yum install -y which git rpm-build && \  
git clone -b "${KM_RELEASE}" https://github.com/yahoo/kafka-manager
/tmp/kafka-manager && \  
cd /tmp/kafka-manager && \  
./sbt rpm:packageBin && \  
yum install -y target/rpm/RPMS/noarch/*.rpm && \  
yum autoremove -y which git rpm-build && \  
yum clean all && \  
rm -rf /root/.sbt /root/.ivy2 /tmp/*  
  
COPY ./start.sh /start.sh  
  
EXPOSE 9000  
CMD ["/start.sh"]  

