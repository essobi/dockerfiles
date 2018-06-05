FROM centos:latest  
  
RUN yum -y update  
  
RUN yum -y install \  
java-1.8.0-openjdk \  
wget  
  
ENV VARSCAN_BIN="VarScan.v2.4.3.jar"  
RUN wget https://github.com/dkoboldt/varscan/raw/master/VarScan.v2.4.3.jar -O
/usr/local/bin/varscan.jar  
  
RUN echo -e "#!/usr/bin/env bash\n\  
java -Xmx8G -jar /usr/local/bin/varscan.jar '$@'\n" \  
>> /usr/local/bin/varscan  
  
RUN chmod +x /usr/local/bin/varscan  

