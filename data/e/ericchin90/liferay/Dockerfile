# VERSION 0.0.1  
# BUILD-USING: docker build -t library/liferay .  
# PUSH-USING: docker tag library/liferay ericchin90/liferay && docker push
ericchin90/liferay  
FROM ericchin90/jdk7  
MAINTAINER Eric Chin <ericchin90@gmail.com>  
  
RUN mkdir /opt/apps  
WORKDIR /opt/apps  
  
RUN echo 'fs.file-max = 100000' >> /etc/sysctl.conf  
  
RUN sed -i.bak '$ i \\*\t\thard\tnofile\t\t8192\n\\*\t\tsoft\tnofile\t\t8192'
/etc/security/limits.conf  
  
RUN wget -q -O liferay.zip https://www.dropbox.com/s/hpnif29834na12u/liferay-
portal-tomcat-6.2-ce-ga2-20140319114139101.zip?dl=0 \  
&& unzip -q liferay.zip \  
&& rm liferay.zip  
  
RUN ln -s /opt/apps/liferay-portal-6.2-ce-ga2 /opt/liferay \  
&& ln -s /opt/liferay/tomcat-7.0.42 /opt/liferay/tomcat  
  
RUN mkdir /opt/liferay/deploy  
  
WORKDIR /opt/liferay  
  
EXPOSE 8080  
ENTRYPOINT ["/opt/liferay/tomcat/bin/catalina.sh"]  
CMD ["run"]  

