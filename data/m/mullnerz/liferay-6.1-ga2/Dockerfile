#  
# Liferay 6.1 GA2 CE Dockerfile  
#  
# https://github.com/mullnerz/docker-images/  
# https://github.com/mullnerz/docker-images/tree/master/liferay-6.1-ga2  
#  
FROM mullnerz/jdk6-oracle  
  
MAINTAINER Zoltán Müllner <mullner.zoltan@gmail.com>  
  
RUN useradd -m -N liferay  
  
WORKDIR /home/liferay  
  
# Install liferay-portal-6.1.1-ce-ga2 and dependencies  
RUN curl -sSL
"http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-tomcat-6.1.1-ce-ga2-20120731132656558.zip" \  
| bsdtar -xf- && \  
chmod +x liferay-portal-6.1.1-ce-ga2/tomcat-7.0.27/bin/*.sh && \  
ln -sf tomcat-7.0.27 liferay-portal-6.1.1-ce-ga2/tomcat && \  
ln -sf /home/liferay/liferay-portal-6.1.1-ce-ga2/ /opt/liferay && \  
ln -sf liferay-portal-6.1.1-ce-ga2 liferay-portal  
  
# Add liferay init-script  
COPY liferay /etc/init.d/  
RUN chmod 755 /etc/init.d/liferay && update-rc.d liferay defaults  
  
EXPOSE 8080  
# Define default command  
CMD service liferay start && tail -f /opt/liferay/tomcat/logs/catalina.out  

