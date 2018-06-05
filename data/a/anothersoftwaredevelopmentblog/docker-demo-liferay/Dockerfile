FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk curl unzip sudo  
RUN apt-get install -y postgresql  
  
RUN curl -O -s -k -L -C -
https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.2%20GA3/liferay-
ce-portal-tomcat-7.0-ga3-20160804222206210.zip  
#ADD liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip /  
RUN unzip liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip  
RUN rm liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip  
  
EXPOSE 8080  
EXPOSE 5432  
RUN ln -s liferay-ce-portal-7.0-ga3 /liferay  
RUN ln -s liferay/tomcat-8.0.32 /tomcat  
  
RUN ln -s liferay/deploy /deploy  
VOLUME /deploy  
  
ADD startup.sh /  
ADD configure-db.sh /  
ADD portal-ext.properties /liferay/  
  
RUN chmod +x /*.sh  
RUN /configure-db.sh  
  
ENTRYPOINT /startup.sh  
  

