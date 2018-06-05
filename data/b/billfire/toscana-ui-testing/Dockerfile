  
FROM openjdk:8-jdk  
  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_SECRET_ACCESS_KEY  
  
ARG MAVEN_VERSION=3.5.2  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
# Install Maven  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
# Set the Chrome repo.  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
  
# Install Chrome.  
RUN apt-get update && apt-get -y install google-chrome-stable  
  
ADD / .  
  
RUN mvn install -DskipTests

