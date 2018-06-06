FROM codearte/openjdk:latest  
  
RUN groupadd -g 2000 crowd && useradd -d /home/crowd -m -g 2000 -u 2000 crowd  
  
WORKDIR /home/crowd  
  
RUN wget http://downloads.atlassian.com/software/crowd/downloads/atlassian-
crowd-2.8.0.tar.gz -O crowd.tgz  
  
RUN mkdir /home/crowd/crowd-app \  
&& tar -xzf crowd.tgz --strip 1 -C /home/crowd/crowd-app \  
&& rm -r crowd.tgz \  
&& echo crowd.home=/home/crowd/crowd-home > /home/crowd/crowd-app/crowd-
webapp/WEB-INF/classes/crowd-init.properties \  
&& mkdir /home/crowd/crowd-home \  
&& chown crowd: -R /home/crowd  
  
USER crowd  
VOLUME /home/crowd/crowd-home  
EXPOSE 8095  
ENTRYPOINT /home/crowd/crowd-app/apache-tomcat/bin/catalina.sh run

