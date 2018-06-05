FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y wget  
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jre-8u111-linux-x64.tar.gz  
  
RUN tar -zxf jre-8u111-linux-x64.tar.gz  
RUN rm jre-8u111-linux-x64.tar.gz  
  
ENV JAVA_HOME /jre1.8.0_111  
  
ENV PATH="${JAVA_HOME}/bin:${PATH}"  
RUN echo ${PATH}  
  
MAINTAINER Denis Kuchugurov, kepkap.dev@gmail.com  
  
ARG jar_name=artwork-application-1.0.0.RELEASE.jar  
  
ADD ./artwork-application/build/libs/${jar_name} .  
RUN mkdir log  
  
RUN ls -la  
RUN java -version  
  
EXPOSE 8080  
ENTRYPOINT ["java", "-jar", "artwork-application-1.0.0.RELEASE.jar"]

