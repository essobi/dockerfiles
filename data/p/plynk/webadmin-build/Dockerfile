FROM openjdk:8-jdk  
MAINTAINER Patrick O'Boyle <patrick@plynk.me>  
  
# Gradle  
ENV GRADLE_VERSION 3.3  
ENV GRADLE_SHA
c58650c278d8cf0696cab65108ae3c8d95eea9c1938e0eb8b997095d5ca9a292  
  
COPY gradle-build.sh /usr/lib/gradle-build.sh  
  
# Installing gradle and other dependencies  
RUN cd /usr/lib \  
&& curl -fl
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o
gradle-bin.zip \  
&& echo "$GRADLE_SHA gradle-bin.zip" | sha256sum -c - \  
&& unzip "gradle-bin.zip" \  
&& ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle \  
&& rm "gradle-bin.zip" \  
&& chmod +x /usr/lib/gradle-build.sh \  
&& ln -s /usr/lib/gradle-build.sh /usr/bin/gradle-build \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends postgresql postgresql-contrib
sudo  
  
# Setting up the test user+db  
RUN service postgresql start \  
&& sudo -u postgres psql -c "CREATE ROLE plynk SUPERUSER CREATEDB CREATEROLE
INHERIT LOGIN PASSWORD 'plynk';" \  
&& sudo -u postgres createdb plynk-clp-test \--owner=plynk  
  
# Add postgres to ssl-cert group so it can run the server  
RUN usermod postgres -g ssl-cert  
  
# Set Appropriate Environmental Variables  
ENV GRADLE_HOME /usr/lib/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Caches  
VOLUME ["/root/.gradle/caches", "/usr/share/app/"]  
  
# Default command is "/usr/lib/gradle-build.sh -version" on /usr/share/app dir  
# (ie. Mount project at /usr/share/app "docker --rm -v
/path/to/app:/usr/share/app plynk/webadmin-build <command>")  
WORKDIR /usr/share/app  
ENTRYPOINT ["gradle-build"]  
CMD ["-version"]  

