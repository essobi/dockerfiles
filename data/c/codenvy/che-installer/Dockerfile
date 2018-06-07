FROM debian:jessie  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -yq wine
wget innoextract wine32 && apt-get clean  
RUN wget http://files.jrsoftware.org/is/5/isetup-5.5.5-unicode.exe &&
innoextract -d /inno /isetup-5.5.5-unicode.exe  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 66  
ENV JAVA_VERSION_BUILD 18  
RUN mkdir /opt/jre-windows && wget -O- --local-encoding=UTF-8 --no-check-
certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-windows-x64.tar.gz
\  
| tar -zx --strip-components=1 -C /opt/jre-windows  
  
ENV GIT_VERSION 2.7.0  
RUN mkdir /opt/git && wget -O /opt/git/git-setup.exe --local-encoding=UTF-8
--no-check-certificate https://github.com/git-for-
windows/git/releases/download/v$GIT_VERSION.windows.1/Git-$GIT_VERSION-64-bit.exe  
  
ENV DOCKER_VERSION 1.10.3  
RUN mkdir /opt/docker && wget --local-encoding=UTF-8 --no-check-certificate -O
/opt/docker/docker-setup.exe
https://github.com/docker/toolbox/releases/download/v$DOCKER_VERSION/DockerToolbox-$DOCKER_VERSION.exe  
  
WORKDIR /user  
ENTRYPOINT ["wine", "/inno/app/ISCC.exe", "/Otarget"]  

