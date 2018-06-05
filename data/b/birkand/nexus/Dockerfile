FROM phusion/baseimage:0.9.15  
MAINTAINER Birkan Duman <birkan.duman@gmail.com>  
RUN apt-get -qq update  
RUN apt-get -qq install openjdk-7-jre-headless  
RUN apt-get -qq install wget  
RUN useradd --user-group --system --home-dir /opt/sonatype-nexus nexus  
RUN mkdir -p /opt/sonatype-nexus  
RUN ["wget", "-O", "/tmp/nexus-latest-bundle.tar.gz",
"http://www.sonatype.org/downloads/nexus-latest-bundle.tar.gz"]  
RUN tar -zxvf /tmp/nexus-latest-bundle.tar.gz -C /opt/sonatype-nexus --strip-
components=1  
RUN chown -R nexus:nexus /opt/sonatype-nexus  
  
ADD assets/init /app/init  
RUN chmod 755 /app/init  
  
VOLUME /opt/sonatype-work  
EXPOSE 8081  
ENTRYPOINT ["/app/init"]  
CMD ["app:start"]

