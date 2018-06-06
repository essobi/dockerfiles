FROM buildpack-deps:jessie-scm  
  
ENV JDL_VERSION "8"  
ENV JDL_UPDATE "141"  
ENV JDL_BUILD "15"  
ENV JDL_SIG "336fa29ff2bb4ef291e347e091f7f4a7"  
  
ENV JAVA_HOME "/usr/lib/jvm/java-${JDL_VERSION}-oracle"  
ENV PATH "$PATH:$JAVA_HOME/bin"  
  
RUN apt-get update \  
&& echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& apt-get update \  
&& apt-get install -y \  
openssh-client \  
ca-certificates \  
tar \  
gzip \  
python-pip \  
apt-transport-https \  
lsb-release \  
&& export DOCKER_VERSION=$(curl --silent --fail --retry 3
https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e
'docker-[.0-9]*-ce\\.tgz' | sort -r | head -n 1) \  
&&
DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}"
\  
&& echo Docker URL: $DOCKER_URL \  
&& curl \--silent \--show-error \--location \--fail \--retry 3 \--output
/tmp/docker.tgz "${DOCKER_URL}" \  
&& ls -lha /tmp/docker.tgz \  
&& tar -xz -C /tmp -f /tmp/docker.tgz \  
&& mv /tmp/docker/* /usr/bin \  
&& curl -LO https://kubernetes-helm.storage.googleapis.com/helm-v2.9.0-linux-
amd64.tar.gz \  
&& tar -xzvf helm-v2.9.0-linux-amd64.tar.gz \  
&& mv linux-amd64/helm /usr/bin/helm \  
&& helm init \--client-only \  
&& helm plugin install https://github.com/nouney/helm-gcs \  
&& rm -rf /tmp/docker /tmp/docker.tgz linux-amd64 \  
&& pip install \--upgrade awscli \  
&& echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \  
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
\  
&& apt-get update \  
&& apt-get install -y google-cloud-sdk kubectl \  
&& curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
-o /tmp/java.tar.gz \  
"http://download.oracle.com/otn-
pub/java/jdk/${JDL_VERSION}u${JDL_UPDATE}-b${JDL_BUILD}/${JDL_SIG}/jdk-${JDL_VERSION}u${JDL_UPDATE}-linux-x64.tar.gz"
\  
&& tar -xvz -C /tmp/ -f /tmp/java.tar.gz \  
&& mkdir -p /usr/lib/jvm \  
&& mv /tmp/jdk1.${JDL_VERSION}.0_${JDL_UPDATE} "${JAVA_HOME}" \  
&& apt-get install sbt \  
&& rm -rf \  
/var/cache/apt/* \  
/tmp/* \  
$JAVA_HOME/*.zip  
  
COPY tools/* /tools/  

