FROM openjdk:10-jdk  
  
# Environment for Bamboo  
ENV BAMBOO_VERSION=6.5.0 \  
BAMBOO_HOME=/home/bamboo  
  
# Expose ports (web/agent)  
EXPOSE 8085 54663  
  
# Add installation script  
ADD resources/bamboo-server.sh /usr/local/bin/bamboo-server.sh  
  
# Install additional dependencies & add execute rights to script  
RUN echo "deb http://deb.debian.org/debian sid main unstable" >
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get upgrade -yq \  
&& apt-get install --no-install-recommends --no-install-suggests -yq
openjdk-8-jdk-headless ssh maven gnupg software-properties-common \  
# Install NodeJS 6.x  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install --no-install-recommends --no-install-suggests -yq nodejs \  
# Clean up  
&& apt-get autoremove -yq \  
&& apt-get autoclean -yq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
# Overrule JAVA_HOME back to JDK8  
&& ln -fsvT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)"
/docker-java-home \  
# Make startup script runnable  
&& chmod +x /usr/local/bin/bamboo-server.sh  
  
VOLUME ["/home/bamboo","/opt/atlassian-bamboo/logs"]  
  
# Run script on start up  
CMD ["/usr/local/bin/bamboo-server.sh"]  

