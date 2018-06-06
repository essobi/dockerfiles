FROM openjdk:8-jdk-alpine  
MAINTAINER 'Siddhartha Basu<sidd.basu@gmail.com>'  
ARG user=cybersiddhu  
  
# Add required softare for intermine  
RUN apk update \  
&& apk add apache-ant --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
RUN apk add git perl bash  
RUN addgroup -g 1000 -S $user && adduser -G $user -D -u 1000 -S $user  
ENV ANT_HOME /usr/share/java/apache-ant  
ENV ANT_OPTS "-server -XX:MaxPermSize=512M -Xmx5g -XX:+UseParallelGC -Xms2g
-XX:SoftRefLRUPolicyMSPerMB=1 -XX:MaxHeapFreeRatio=99"  
USER $user  
WORKDIR /home/$user  
RUN mkdir -p /home/$user/dictymine-commands/src /home/$user/dictymine-
commands/gradle  
COPY gradle /home/$user/dictymine-commands/gradle/  
COPY src /home/$user/dictymine-commands/src/  
COPY build.gradle /home/$user/dictymine-commands/  
COPY settings.gradle /home/$user/dictymine-commands/  
COPY gradlew /home/$user/dictymine-commands/  
RUN cd /home/$user/dictymine-commands \  
&& ./gradlew installDist  
ENV PATH $PATH:$ANT_HOME/bin:/home/$user/dictymine-
commands/build/install/dictyMine/bin  

