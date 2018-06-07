FROM openjdk:8-jdk  
LABEL maintainer="Ruben Anders <rubenanders@outlook.de>"  
  
ENV GRADLE_VERSION 4.4.1  
RUN TMPFILE="$(mktemp)" && \  
wget
"https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"
-O "$TMPFILE" && \  
unzip "$TMPFILE" -d "/usr/local" && \  
mv "/usr/local/gradle-${GRADLE_VERSION}" "/usr/local/gradle" && \  
ln -s "../gradle/bin/gradle" "/usr/local/bin/gradle" && \  
rm "$TMPFILE"  
  
RUN mkdir ~/.gradle && \  
echo "org.gradle.daemon=false" > ~/.gradle/gradle.properties  

