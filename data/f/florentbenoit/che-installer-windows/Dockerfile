FROM debian:jessie  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -yq wine
wget innoextract wine32 && apt-get clean  
RUN wget http://files.jrsoftware.org/is/5/isetup-5.5.5-unicode.exe &&
innoextract -d /inno /isetup-5.5.5-unicode.exe  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 60  
ENV JAVA_VERSION_BUILD 27  
ENV MAVEN_VERSION 3.3.3  
RUN mkdir /opt/apache-maven && wget -qO- --local-encoding=UTF-8
http://repo1.maven.org/maven2/org/apache/maven/apache-
maven/${MAVEN_VERSION}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
| tar -zx --strip-components=1 -C /opt/apache-maven  
  
RUN mkdir /opt/jdk-windows  
RUN wget --local-encoding=UTF-8 --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/jdk-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-windows-x64.exe  
  
RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-
free" >> /etc/apt/sources.list  
RUN apt-get update && apt-get install -y p7zip-full unzip openjdk-8-jdk  
  
RUN 7z x /jdk-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-windows-x64.exe &&
unzip /tools.zip -d /opt/jdk-windows/  
WORKDIR /opt/jdk-windows  
RUN find /opt/jdk-windows/ -type f -name "*.pack" | while read eachFile; do
echo "Unpacking $eachFile ..."; /usr/bin/unpack200 $eachFile
${eachFile%.pack}.jar; rm $eachFile; done  
RUN find /opt/jdk-windows -type f \\( -name "*.exe" -o -name "*.dll" \\) -exec
chmod u+rwx {} \;  
  
RUN mkdir /opt/jre-windows && wget -O- --local-encoding=UTF-8 --no-check-
certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-windows-x64.tar.gz
\  
| tar -zx --strip-components=1 -C /opt/jre-windows  
  
# as per redistribution section, we can embed javac inside a JRE with the same
version  
#
http://www.oracle.com/technetwork/java/javase/readme-142177.html#redistribution  
RUN cp /opt/jdk-windows/bin/javac.exe /opt/jre-windows/bin/javac.exe  
RUN cp /opt/jdk-windows/lib/tools.jar /opt/jre-windows/lib/tools.jar  
  
ENV GIT_VERSION 2.5.2  
RUN mkdir /opt/git && wget -O /opt/git/git-setup.exe --local-encoding=UTF-8
--no-check-certificate https://github.com/git-for-
windows/git/releases/download/v$GIT_VERSION.windows.2/Git-$GIT_VERSION.2-64-bit.exe  
  
ENV DOCKER_VERSION 1.8.2  
RUN mkdir /opt/docker && wget --local-encoding=UTF-8 --no-check-certificate -O
/opt/docker/docker-setup.exe
https://github.com/docker/toolbox/releases/download/v1.8.2/DockerToolbox-1.8.2.exe  
  
WORKDIR /user  
ENTRYPOINT ["wine", "/inno/app/ISCC.exe", "/Otarget"]  

