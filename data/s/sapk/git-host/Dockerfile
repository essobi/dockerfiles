FROM java:8-jre  
  
MAINTAINER Antoine GIRARD <antoine.girard [at] sapk.fr>  
  
RUN wget "$(wget -nv https://github.com/takezoe/gitbucket/releases/latest/ -O
/dev/null 2>&1 | sed 's/.*\URL:\\(https.*\\) \\[.*\\] .*/\1/' | sed
's/tag/download/')/gitbucket.war" -O /opt/gitbucket.war  
  
# adduser --quiet --shell /bin/false --disabled-login --home /data git && ls
-lah /data  
VOLUME ["/data"]  
  
# Port for web page  
EXPOSE 8080  
# Port for SSH access to git repository (Optional)  
EXPOSE 22  
#USER git  
#We need to choose a option to run as the git with the same uid as the host  
ENTRYPOINT ["/usr/bin/java", "-jar", "/opt/gitbucket.war", "--
gitbucket.home=/data", "--port=8080", "--prefix=/"]  
  

