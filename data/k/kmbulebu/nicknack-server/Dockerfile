FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get install openjdk-7-jre-headless -y  
  
ADD
http://search.maven.org/remotecontent?filepath=com/github/kmbulebu/nicknack/nicknack-
server-assembly/0.0.7/nicknack-server-assembly-0.0.7-distribution.tar.gz
/tmp/nicknack.tar.gz  
  
RUN mkdir -p /opt  
RUN tar xvzf /tmp/nicknack.tar.gz -C /opt/  
  
EXPOSE 8085  
CMD /opt/nicknack/bin/nicknack console  

