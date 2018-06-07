FROM java:7-jdk  
  
# Gradle  
ENV GRADLE_VERSION 1.12  
ENV GRADLE_SHA
8734b13a401f4311ee418173ed6ca8662d2b0a535be8ff2a43ecb1c13cd406ea  
  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip" \  
&& mkdir -p /usr/src/app  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/src/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/bin/app"]  
  
# Default command is "/usr/bin/gradle -version" on /usr/bin/app dir  
# (ie. Mount project at /usr/bin/app "docker --rm -v /path/to/app:/usr/bin/app
gradle <command>")  
WORKDIR ["/usr/bin/app"]  
ENTRYPOINT ["gradle"]  
CMD ["-version"]  

