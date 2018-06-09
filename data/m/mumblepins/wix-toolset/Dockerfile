FROM buildpack-deps:xenial-scm  
  
ENV MAVEN_VERSION=3.5.2 \  
ANT_VERSION=1.10.1 \  
GRADLE_VERSION=4.4.1  
  
RUN set -ex; \  
dpkg \--add-architecture i386 ;\  
apt-get update ;\  
apt-get install -y \--no-install-recommends apt-transport-https ;\  
wget -nc https://dl.winehq.org/wine-builds/Release.key ;\  
apt-key add Release.key ;\  
echo "deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main" >>
/etc/apt/sources.list ;\  
mkdir -p /usr/share/man/man1 /etc/apt/sources.list.d ;\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list ;\  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list ;\  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
;\  
apt-get update ;\  
apt-get install -y \--no-install-recommends\  
binutils \  
cabextract \  
p7zip \  
unzip \  
wget \  
file \  
git \  
mercurial xvfb locales sudo openssh-client ca-certificates tar gzip parallel
net-tools netcat unzip zip bzip2 gnupg curl wget \  
snapcraft ;\  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections ;\  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections ;\  
apt-get install -y \--no-install-recommends oracle-java9-installer ;\  
apt-get install -y \--no-install-recommends winehq-stable ;\  
ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime ;\  
apt-get dist-upgrade -y ;\  
apt-get autoremove -y ;\  
apt-get clean -y ;\  
rm -rf /var/lib/apt/lists/*  
  
  
RUN set -ex; \  
export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) ;\  
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
;\  
echo Docker URL: $DOCKER_URL ;\  
curl \--silent \--show-error \--location \--fail \--retry 3 \--output
/tmp/docker.tgz "${DOCKER_URL}" ;\  
ls -lha /tmp/docker.tgz ;\  
tar -xz -C /tmp -f /tmp/docker.tgz ;\  
mv /tmp/docker/* /usr/bin ;\  
rm -rf /tmp/docker /tmp/docker.tgz ;\  
which docker ;\  
(docker version || true)  
  
RUN set -ex ;\  
curl -SL
'https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks'
-o /usr/local/bin/winetricks; \  
chmod +x /usr/local/bin/winetricks  
  
RUN curl \--silent \--show-error \--location \--fail \--retry 3 \--output
/tmp/apache-maven.tar.gz \  
https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar xf /tmp/apache-maven.tar.gz -C /opt/ \  
&& rm /tmp/apache-maven.tar.gz \  
&& ln -s /opt/apache-maven-* /opt/apache-maven \  
&& /opt/apache-maven/bin/mvn -version  
# Install Ant Version: $ANT_VERSION  
RUN curl \--silent \--show-error \--location \--fail \--retry 3 \--output
/tmp/apache-ant.tar.gz \  
https://archive.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz \  
&& tar xf /tmp/apache-ant.tar.gz -C /opt/ \  
&& ln -s /opt/apache-ant-* /opt/apache-ant \  
&& rm -rf /tmp/apache-ant.tar.gz \  
&& /opt/apache-ant/bin/ant -version  
ENV ANT_HOME=/opt/apache-ant  
# Install Gradle Version: $GRADLE_VERSION  
RUN curl \--silent \--show-error \--location \--fail \--retry 3 \--output
/tmp/gradle.zip \  
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip -d /opt /tmp/gradle.zip \  
&& rm /tmp/gradle.zip \  
&& ln -s /opt/gradle-* /opt/gradle \  
&& /opt/gradle/bin/gradle -version  
  
ENV PATH="/opt/sbt/bin:/opt/apache-maven/bin:/opt/apache-
ant/bin:/opt/gradle/bin:$PATH"  
  
RUN set -ex ;\  
cd /tmp ;\  
mkdir -p ivy ;\  
cd ivy ;\  
curl -sSL
http://mirror.cc.columbia.edu/pub/software/apache//ant/ivy/2.4.0/apache-
ivy-2.4.0-bin.tar.gz | tar xvz \--strip-components=1 ;\  
cp ivy-*.jar $ANT_HOME/lib/ ;\  
cd .. ;\  
rm -rf ivy ;\  
cd $ANT_HOME ;\  
ant -f fetch.xml -Ddest=system ;\  
useradd -d /home/wix -m -s /bin/bash wix  
  
USER wix  
ENV HOME=/home/wix \  
WINEPREFIX=/home/wix/.wine \  
WINEARCH=win32  
  
WORKDIR /home/wix  
  
RUN set -ex ;\  
wine wineboot ;\  
xvfb-run winetricks \--unattended dotnet40 corefonts ;\  
wget -O wix-binaries.zip
https://github.com/wixtoolset/wix3/releases/download/wix3111rtm/wix311-binaries.zip
;\  
unzip wix-binaries.zip ;\  
rm -rf wix-binaries.zip doc sdk  
  
USER root  
  
RUN set -ex; \  
for a in $(find /home/wix -maxdepth 1 -iname '*.exe' ); do \  
b=$(echo "$a" | sed -r 's|^.*/([^.]*).exe$|\1|'); \  
echo '#!/bin/bash' > "/usr/local/bin/$b"; \  
echo "wine $a"' "$@"' >> "/usr/local/bin/$b"; \  
chmod +x "/usr/local/bin/$b" ;\  
done  
  
USER wix  
  
  
ENTRYPOINT ["/bin/bash"]  

