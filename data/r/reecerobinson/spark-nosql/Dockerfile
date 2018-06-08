From reecerobinson/spark-base:1.6.0  
MAINTAINER docker@reecerobinson.co.nz  
  
COPY pom.xml /root/pom.xml  
WORKDIR /root  
  
RUN wget
http://ppa.launchpad.net/natecarlson/maven3/ubuntu/pool/main/m/maven3/maven3_3.2.1-0~ppa1_all.deb
&& \  
gdebi -n maven3_3.2.1-0~ppa1_all.deb && \  
ln -s /usr/share/maven3/bin/mvn /usr/bin/mvn && \  
rm maven3_3.2.1-0~ppa1_all.deb  
  
RUN mvn dependency:copy-dependencies  
RUN cp /root/target/dependency/* /usr/local/spark/lib  
COPY spark-defaults.conf /usr/local/spark/conf/spark-defaults.conf  

