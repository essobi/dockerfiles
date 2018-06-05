FROM maven:3-jdk-8 as builder  
  
RUN set -x \  
&& addgroup cakeshop \  
&& useradd -g cakeshop -s /bin/bash --home-dir /home/cakeshop -m cakeshop  
  
USER cakeshop  
  
RUN mkdir -p $HOME/.m2  
  
ENV USER_HOME_DIR "/home/cakeshop"  
ENV MAVEN_CONFIG "/home/cakeshop/.m2"  
RUN cd /home/cakeshop && \  
git clone https://github.com/zean00/cakeshop --depth 1  
RUN cd /home/cakeshop/cakeshop && mvn -DskipTests clean package  
  
FROM openjdk:8-jdk  
  
RUN set -x \  
&& addgroup cakeshop \  
&& useradd -g cakeshop -s /bin/bash --home-dir /home/cakeshop -m cakeshop  
  
COPY \--from=builder \  
/home/cakeshop/cakeshop/cakeshop-api/target/cakeshop-0.10.0.war \  
/home/cakeshop/cakeshop/docker/cakeshop/application.properties \  
/home/cakeshop/cakeshop/docker/cakeshop/cakeshop.sh \  
/home/cakeshop/  
  
#COPY cakeshop.sh /home/cakeshop/  
RUN chmod +x /home/cakeshop/cakeshop.sh  
  
# for main web interface:  
EXPOSE 8080  
# will be used by attached slave agents:  
EXPOSE 8102  
WORKDIR /home/cakeshop  
CMD ["/bin/sh","/home/cakeshop/cakeshop.sh"]

