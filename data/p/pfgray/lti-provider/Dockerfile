FROM library/ubuntu  
  
#install java  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y wget  
  
#install tomcat  
WORKDIR /opt  
RUN wget http://mirrors.gigenet.com/apache/tomcat/tomcat-8/v8.0.32/bin/apache-
tomcat-8.0.32.tar.gz  
RUN tar -zxvf apache-tomcat-8.0.32.tar.gz  
RUN mv apache-tomcat-8.0.32 tomcat  
  
#install Maven  
RUN apt-get install -y maven  
  
#build mock-rest  
WORKDIR /root  
ADD ./ /root/lti-example  
WORKDIR /root/lti-example  
RUN mvn clean install  
  
#configure mock-rest to be the root of its virtual host  
WORKDIR /opt/tomcat  
ADD ./config/server.xml /opt/tomcat/conf/server.xml  
RUN rm -rf webapps/*  
  
#deploy mock-rest  
RUN cp /root/lti-example/target/ExampleLtiApp*.war
/opt/tomcat/webapps/ROOT.war  
  
#run tomcat  
WORKDIR /opt/tomcat/bin  
ADD ./run.sh /usr/local/bin/run  
EXPOSE 8080  
CMD ["/bin/sh", "-e", "/usr/local/bin/run"]  

