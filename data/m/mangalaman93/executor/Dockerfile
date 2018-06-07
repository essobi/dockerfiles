FROM mangalaman93/spark:2.1.0  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r hadoop \--gid=1000 && useradd -r -g hadoop -d /home/hadoop
\--uid=1000 hadoop  
  
RUN mkdir -p /home/hadoop && \  
chown -R hadoop:hadoop /home/hadoop  
  
VOLUME /opt/spark/tmp  
WORKDIR /home/hadoop  
USER hadoop  

