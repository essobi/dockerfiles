FROM openjdk:8-alpine  
RUN apk add -U --no-cache curl ca-certificates  
ENV LIFERAY_HOME=/opt/liferay  
ENV LIFERAY_PROPERTIES_URL=''  
EXPOSE 8080/tcp  
WORKDIR /opt  
RUN set -x && \  
curl -fSL
https://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.2.5%20GA6/liferay-
portal-tomcat-6.2-ce-ga6-20160112152609836.zip/download -o liferay.zip && \  
unzip liferay.zip && \  
mv liferay-portal-6.2-ce-ga6 liferay && \  
rm liferay.zip  
COPY assets/run.sh /opt/liferay/run.sh  
VOLUME /opt/liferay  
CMD ["/opt/liferay/run.sh"]  

