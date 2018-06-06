FROM anapsix/alpine-java:7_jdk  
MAINTAINER kaakaa <stooner.hoe@gmail.com>  
  
RUN apk update  
  
RUN apk add wget unzip fontconfig libreoffice  
RUN wget -O ipa-font.zip
'https://osdn.jp/frs/redir.php?m=iij&f=%2Fipafonts%2F51868%2FIPAfont00303.zip'  
RUN mkdir /root/.fonts \  
&& unzip ipa-font.zip -d /root/.fonts \  
&& rm -fr ipa-font.zip  
RUN fc-cache -fv  
  
RUN wget -O jod-tomcat.zip
'http://sourceforge.net/projects/jodconverter/files/JODConverter/2.2.2/jodconverter-
tomcat-2.2.2.zip/download'  
RUN unzip jod-tomcat.zip -d /usr/local/src \  
&& ln -s /usr/local/src/jodconverter-tomcat-2.2.2/bin/startup.sh /usr/bin/jod
\  
&& rm jod-tomcat.zip  
  
ADD start /usr/bin/start-jod  
ADD applicationContext.xml /usr/local/src/jodconverter-
tomcat-2.2.2/webapps/converter/WEB-INF/applicationContext.xml  
  
RUN chmod -R 777 /usr/bin/  
  
EXPOSE 8080  
ENTRYPOINT ["/bin/sh", "-c", "/usr/bin/start-jod"]  

