FROM codenvy/shellinabox  
  
RUN wget \  
\--no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
-qO- \  
"http://download.oracle.com/otn-
pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.tar.gz" | sudo tar -zx -C /opt/  
  
RUN sudo apt-get update && sudo apt-get install -y git curl subversion  
  
ENV JAVA_HOME /opt/jdk1.8.0_51  
RUN echo "export JAVA_HOME=$JAVA_HOME" >> /home/user/.bashrc  
ENV PATH $JAVA_HOME/bin:$PATH  
RUN echo "export PATH=$PATH" >> /home/user/.bashrc  
RUN mkdir /opt/automation  
ADD automation /opt/automation  
RUN cd /opt/automation/ && ./cbuild --install  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /opt \  
&& mv /opt/apache-maven-$MAVEN_VERSION /opt/maven \  
&& sudo ln -s /opt/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
RUN cbuild -l che-parent che-core che-plugins che --nobuild --t -maven-
additional-params '-Dfindbugs.skip=true'  
RUN cd $HOME/che-core && mvn install -Dfindbugs.skip=true
-Dmaven.test.skip=true  
RUN cd $HOME/che-plugins && mvn install -Dfindbugs.skip=true
-Dmaven.test.skip=true  
RUN cd $HOME/che && mvn dependency:copy-dependencies && mvn validate  

