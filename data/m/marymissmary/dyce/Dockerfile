##  
## Main dockerfile for project  
##  
## see: https://github.com/docker-library/docs/blob/master/tomcat/tag-
details.md#tomcatjre8  
FROM tomcat:jre8  
  
MAINTAINER marohrdanz@mdanderson.org  
  
ENV PATH /usr/local/tomcat/bin:$PATH  
  
WORKDIR /usr/local/tomcat  
  
##  
## Put the pre-built dyce war file in palce.  
##  
COPY dyce_source/target/dyce.war /usr/local/tomcat/webapps/dyce.war  
  
##  
## Get script for modifying the server config file  
##  
COPY dyce_source/modify_DyCE_configuration.sh
/usr/bin/modify_DyCE_configuration.sh  
  
EXPOSE 8080  
##  
## use custom intro web page:  
##  
COPY tomcat_customizations/index.jsp /usr/local/tomcat/webapps/ROOT/index.jsp  
COPY tomcat_customizations/tomcat.css
/usr/local/tomcat/webapps/ROOT/tomcat.css  
  
##  
## put in images for intro web page:  
##  
COPY tomcat_customizations/images /usr/local/tomcat/webapps/ROOT/images  
  
##  
## Make symbolic link from the loaded volume of web pages to  
## the Tomcat document root  
##  
RUN ln -s /usr/local/dyce/apps /usr/local/tomcat/webapps/apps  
  
##  
## Add customized logging  
##  
COPY tomcat_customizations/log4j.properties
/usr/local/tomcat/lib/log4j.properties  
  
##  
## Add JAR file for JSTL  
##  
COPY tomcat_customizations/jstl-1.2.jar /usr/local/tomcat/lib/jstl-1.2.jar  
  
## make things pretty  
RUN apt-get update && apt-get install -y vim  
RUN echo "syntax on" > /root/.vimrc  
RUN echo ":set hlsearch" >> /root/.vimrc  
RUN echo ":set ruler" >> /root/.vimrc  
  
RUN echo 'alias ls="ls --color=auto"' > /root/.alias  
  
RUN echo "source ~/.alias" > /root/.bashrc  
RUN echo 'export PS1="\033[0;34m\u@dyce:/# \033[0m"' >> /root/.bashrc  
  
##  
## run Tomcat on startup  
##  
CMD ["catalina.sh", "run"]  

