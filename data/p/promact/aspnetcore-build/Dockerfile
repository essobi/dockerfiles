FROM microsoft/dotnet:2.0.7-sdk-2.1.200-stretch  
  
# set up environment  
ENV ASPNETCORE_URLS http://+:80  
ENV ASPNETCORE_PKG_VERSION 2.0.8  
# set up node  
ENV NODE_VERSION 8.11.2  
ENV NODE_DOWNLOAD_SHA
67dc4c06a58d4b23c5378325ad7e0a2ec482b48cea802252b99ebe8538a3ab79  
ENV NODE_DOWNLOAD_URL
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz  
  
RUN curl -SL "$NODE_DOWNLOAD_URL" \--output nodejs.tar.gz \  
&& echo "$NODE_DOWNLOAD_SHA nodejs.tar.gz" | sha256sum -c - \  
&& tar -xzf "nodejs.tar.gz" -C /usr/local \--strip-components=1 \  
&& rm nodejs.tar.gz \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest && chmod +x /usr/local/bin/ecs-cli  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables \  
bzip2 \  
python-pip \  
unzip \  
python-setuptools jq \  
\--no-install-recommends  
  
RUN curl -sSL https://get.docker.com/ | sh  
  
RUN pip install awscli --upgrade  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe  
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)"
/docker-java-home  
ENV JAVA_HOME /docker-java-home/jre  
  
ENV JAVA_VERSION 8u171  
ENV JAVA_DEBIAN_VERSION 8u171-b11-1~deb9u1  
  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20170531+nmu1  
  
RUN set -ex; \  
\  
# deal with slim variants not having man page directories (which causes
"update-alternatives" to fail)  
if [ ! -d /usr/share/man/man1 ]; then \  
mkdir -p /usr/share/man/man1; \  
fi; \  
\  
apt-get update; \  
apt-get install -y \  
openjdk-8-jre="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
# verify that "docker-java-home" returns what we expect  
[ "$(readlink -f "$JAVA_HOME")" = "$(docker-java-home)" ]; \  
\  
# update-alternatives so that future installs of other OpenJDK versions don't
change /usr/bin/java  
update-alternatives --get-selections | awk -v home="$(readlink -f
"$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-
alternatives --set-selections" }'; \  
# ... and verify that it actually worked for one of the alternatives we care
about  
update-alternatives --query java | grep -q 'Status: manual'  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
RUN curl -sSL https://github.com/SonarSource/sonar-scanner-
msbuild/releases/download/4.2.0.1214/sonar-scanner-
msbuild-4.2.0.1214-netcoreapp2.0.zip --output sonar.zip \  
&& unzip sonar.zip -d /opt/sonar \  
&& rm -rf sonar.zip

