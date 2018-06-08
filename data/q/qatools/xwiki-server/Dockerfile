from dockerfile/java:oracle-java7  
maintainer Baev Dmitry  
  
RUN wget -q "http://maven.xwiki.org/public.gpg" -O- | sudo apt-key add -  
RUN wget "http://maven.xwiki.org/stable/xwiki-stable.list" -P
/etc/apt/sources.list.d/  
  
RUN apt-get update && apt-get install -y tomcat7 xwiki-enterprise-tomcat-
common  

