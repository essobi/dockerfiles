FROM openjdk:8-jdk  
  
  
ENV MAVEN_VERSION=3.3.9  
ENV MAVEN_HOME=/usr/share/maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-${MAVEN_VERSION} /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
  
ENV ANT_VERSION=1.10.0  
ENV ANT_HOME=/usr/share/ant  
  
RUN curl -fsSL http://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-ant-${ANT_VERSION} /usr/share/ant \  
&& ln -s /usr/share/ant/bin/ant /usr/bin/ant  
  
  
ENV INY_VERSION=2.4.0  
ENV INY_HOME=/usr/share/ivy  
  
RUN curl -fsSL http://archive.apache.org/dist/ant/ivy/${INY_VERSION}/apache-
ivy-${INY_VERSION}-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-ivy-${INY_VERSION} /usr/share/ivy \  
&& cp /usr/share/ivy/ivy-${INY_VERSION}.jar /usr/share/ant/lib  
  
WORKDIR /root  

