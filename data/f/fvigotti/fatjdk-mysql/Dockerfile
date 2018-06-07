FROM fvigotti/docker-fatjdk8:latest  
  
# install mariadb client  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv
0xcbcb082a1bb943db && \  
echo "deb http://mariadb.mirror.iweb.com/repo/10.1/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/mariadb.list && \  
apt-get update && \  
apt-get install -y mariadb-client  
  
  
  
#WORKDIR /opt  
  
#ENTRYPOINT ["java", "-jar", "/whatever/your.jar"]  
  

