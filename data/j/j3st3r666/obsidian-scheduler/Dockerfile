FROM tomcat:jre8  
  
ADD http://obsidianscheduler.com/obsidian-4.1.0.zip /install/  
COPY obsidian-installation.xml /install/  
WORKDIR /install  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get clean && \  
unzip obsidian-4.1.0.zip && \  
java -jar Obsidian-Install-4.1.0.jar obsidian-installation.xml && \  
mv /usr/local/tomcat/webapps/ROOT /usr/local/tomcat/webapps/ROOT.bak && \  
ln -s /usr/share/obsidian/obsidian.war /usr/local/tomcat/webapps/ROOT.war  
  
WORKDIR $CATALINA_HOME  
  
VOLUME /mnt/db/obsidian  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

