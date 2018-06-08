# We use Ubuntu 14.04.4 LTS  
FROM ubuntu:14.04.4  
  
# We update the OS  
RUN apt-get update && apt-get upgrade -y  
  
# We install Java 7  
RUN apt-get install openjdk-7-jdk -y  
  
# We install unzip  
RUN apt-get install unzip -y  
  
# We install wget  
RUN apt-get install wget -y  
  
# We deploy JBoss 5.0.1 GA  
ADD components/jboss-5.0.1.GA /usr/local/share/jboss-5.0.1.GA  
  
# We deploy JTDS (SQL Server Driver) required for database access  
ADD components/jtds-1.2.2-dist/jtds-1.2.2.jar
/usr/local/share/jboss-5.0.1.GA/server/default/lib/  
  
# We disable ROOT.war to avoid having the JBOSS home page with all details  
RUN mv /usr/local/share/jboss-5.0.1.GA/server/default/deploy/ROOT.war
/usr/local/share/jboss-5.0.1.GA/server/default/deploy/ROOT.war.bak

