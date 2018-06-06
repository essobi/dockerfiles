  
FROM ubuntu:18.04  
  
ARG build_fileserver  
ENV ARIA2C_DOWNLOAD aria2c --file-allocation=none -c -x 10 -s 10 -m 0
\--console-log-level=notice --log-level=notice --summary-interval=0  
#wget -q -O ${target} ${url} or ${ARIA2C_DOWNLOAD} -o ${target} ${url}  
## install tools  
RUN set -ex \  
&& sed -i
's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y apt-transport-https apt-utils aria2 ca-certificates curl
git httpie lsb-release nano software-properties-common unzip vim wget \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
## locale  
RUN set -ex \  
&& echo 'tzdata tzdata/Areas select Asia\n\  
tzdata tzdata/Zones/Asia select Shanghai\n\n\  
locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8\n\  
locales locales/default_environment_locale select en_US.UTF-8\n' >
/etc/debconf.txt \  
&& apt-get update -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get -yq install --reinstall locales
tzdata debconf \  
&& debconf-set-selections /etc/debconf.txt \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& dpkg-reconfigure -f noninteractive locales \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
## install global node.js  
RUN if [ -z "${build_fileserver}" ]; then
build_fileserver="https://nodejs.org"; fi \  
&& NODE_VERSION="v9.11.1" \  
&& mkdir -p /opt \  
&& ${ARIA2C_DOWNLOAD} -o node-${NODE_VERSION}-linux-x64.tar.xz
${build_fileserver}/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz
\  
&& tar xf node-${NODE_VERSION}-linux-x64.tar.xz -C /opt \  
&& ln -sf /opt/node-${NODE_VERSION}-linux-x64 /opt/node \  
&& rm -f node-${NODE_VERSION}-linux-x64.tar.xz  
## install node.js for current user  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash \  
&& touch ~/.bash_profile \  
&& echo 'export NVM_DIR="$HOME/.nvm"\n\  
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" # This loads nvm\n\  
[ -s "$NVM_DIR/bash_completion" ] && \\. "$NVM_DIR/bash_completion" # This
loads nvm bash_completion\  
' >> ~/.bash_profile \  
&& . ~/.nvm/nvm.sh \  
&& NVM_NODEJS_ORG_MIRROR="https://npm.taobao.org/mirrors/node" \  
&& NVM_IOJS_ORG_MIRROR="https://npm.taobao.org/mirrors/iojs" \  
&& nvm install 9.11.1  
  
## install global python  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y build-essential python python-pip \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
## install python for current user  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y build-essential git libbz2-dev libreadline-dev
libsqlite3-dev libssl-dev make python python-pip zlib1g-dev \  
&& curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-
installer | bash \  
&& touch ~/.bash_profile \  
&& echo 'export PATH="${HOME}/.pyenv/bin:$PATH"' >> ~/.bash_profile \  
&& echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; eval
"$(pyenv virtualenv-init -)"; fi' >> ~/.bash_profile \  
&& /bin/bash --login -c "pyenv install 2.7.14 && pyenv install 3.6.5" \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
## install global ruby  
# see: https://gorails.com/setup/ubuntu/18.04  
RUN set -ex \  
&& apt-get update -y \  
&& apt-get install -y libgdbm-dev libncurses5-dev automake libtool bison
libffi-dev \  
&& for key in \  
409B6B1796C275462A1703113804BB82D39DC0E3 \  
7D2BAF1CF37B13E2069D6956105BD0E739499BDB \  
; do \  
gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& gpg --keyserver hkp://keys.gnupg.net --recv-keys \  
&& curl -L https://get.rvm.io | bash -s stable --auto-dotfiles \  
&& touch ~/.bash_profile \  
&& echo '[[ -s "/usr/local/rvm/scripts/rvm" ]] && source
"/usr/local/rvm/scripts/rvm"' >> ~/.bash_profile \  
&& /bin/bash --login -c "rvm install ruby-2.4.1 && rvm use ruby-2.4.1
\--default && ruby -v" \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
## install docker, docker-machine, docker-compose  
# Select docker version both supported by rancher and kubernetes  
# see: https://docs.rancher.com/rancher/v1.6/en/hosts/#supported-docker-
versions  
# see: https://github.com/gitlawr/install-docker  
# 1.12  
#apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
# && echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee
/etc/apt/sources.list.d/docker.list \  
# && apt-get update \  
# && apt-cache madison docker-engine \  
# && apt-get -yq install docker-engine=1.12.6-0~ubuntu-xenial  
#curl -sSL https://github.com/gitlawr/install-
docker/blob/master/1.12.6.sh?raw=true | sh  
#  
# 17.03  
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
# && add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \  
# && apt-get update \  
# && apt-cache madison docker-ce \  
# && apt-get -yq --allow-unauthenticated install docker-
ce=17.03.1~ce-0~ubuntu-xenial  
#curl -sSL https://github.com/gitlawr/install-
docker/blob/1.0/17.03.1.sh?raw=true | sh  
#  
#STABLE (NOT YET AVAILABLE!), please check availabilty before using:  
#echo 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic
stable' > /etc/apt/sources.list.d/docker.list  
#echo 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic edge'
>> /etc/apt/sources.list.d/docker.list  
#echo 'deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic
nightly' >> /etc/apt/sources.list.d/docker.list  
# or  
#add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable"  
#add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) edge"  
#add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) nightly"  
# then  
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
# or  
#${ARIA2C_DOWNLOAD} -d /tmp -o docker_ubuntu_gpg
https://download.docker.com/linux/ubuntu/gpg && apt-key add
/tmp/docker_ubuntu_gpg  
COPY docker/docker_ubuntu_gpg /tmp/docker_ubuntu_gpg  
RUN set -ex \  
&& groupadd -f docker \  
&& apt-key add /tmp/docker_ubuntu_gpg && rm -f /tmp/docker_ubuntu_gpg \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) edge" \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) nightly" \  
&& apt-get update -y \  
&& apt-get -yq install apt-transport-https ca-certificates curl software-
properties-common \  
&& apt-cache madison docker-ce \  
&& apt-get -yq install docker-ce=18.05.0~ce~3-0~ubuntu \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin \  
&& if [ -z "${build_fileserver}" ]; then
build_fileserver="http://o9wbz99tz.bkt.clouddn.com"; fi \  
&& ${ARIA2C_DOWNLOAD} -o /usr/local/bin/docker-machine
${build_fileserver}/docker/machine/releases/download/v0.14.0/docker-machine-
Linux-x86_64 \  
&& chmod +x /usr/local/bin/docker-machine \  
&& ${ARIA2C_DOWNLOAD} -o /usr/local/bin/docker-compose
${build_fileserver}/docker/compose/releases/download/1.21.2/docker-compose-
Linux-x86_64 \  
&& chmod +x /usr/local/bin/docker-compose  
  
## install jdk8  
# http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz  
#curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
# ${build_fileserver}/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE_DIGEST}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
# | tar -xzf - -C /opt \  
ENV JDK8_HOME /usr/lib/jvm/java-8-oracle  
RUN JAVA_VERSION_MAJOR=8 \  
&& JAVA_VERSION_MINOR=171 \  
&& JAVA_VERSION_BUILD=11 \  
&& JAVA_PACKAGE=jdk \  
&& JAVA_PACKAGE_DIGEST=512cd62ec5174c3487ac17c61aaa89e8 \  
&& if [ -z "${build_fileserver}" ]; then
build_fileserver="http://download.oracle.com"; fi \  
&& mkdir -p $(dirname ${JDK8_HOME}) \  
&& ${ARIA2C_DOWNLOAD} --header="Cookie: oraclelicense=accept-securebackup-
cookie" -d /tmp -o
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
${build_fileserver}/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE_DIGEST}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
&& tar -xzf
/tmp/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-C $(dirname ${JDK8_HOME}) \  
&& rm -rf /tmp/jdk* \  
&& mv $(dirname
${JDK8_HOME})/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JDK8_HOME}
\  
&& mkdir -p
/Library/Java/JavaVirtualMachines/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}.jdk/Contents
\  
&& ln -s ${JDK8_HOME}
/Library/Java/JavaVirtualMachines/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}.jdk/Contents/Home
\  
&& rm -rf ${JDK8_HOME}/*src.zip \  
${JDK8_HOME}/lib/missioncontrol \  
${JDK8_HOME}/lib/visualvm \  
${JDK8_HOME}/lib/*javafx* \  
${JDK8_HOME}/jre/lib/plugin.jar \  
${JDK8_HOME}/jre/lib/ext/jfxrt.jar \  
${JDK8_HOME}/jre/bin/javaws \  
${JDK8_HOME}/jre/lib/javaws.jar \  
${JDK8_HOME}/jre/lib/desktop \  
${JDK8_HOME}/jre/plugin \  
${JDK8_HOME}/jre/lib/deploy* \  
${JDK8_HOME}/jre/lib/*javafx* \  
${JDK8_HOME}/jre/lib/*jfx* \  
${JDK8_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JDK8_HOME}/jre/lib/amd64/libprism_*.so \  
${JDK8_HOME}/jre/lib/amd64/libfxplugins.so \  
${JDK8_HOME}/jre/lib/amd64/libglass.so \  
${JDK8_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JDK8_HOME}/jre/lib/amd64/libjavafx*.so \  
${JDK8_HOME}/jre/lib/amd64/libjfx*.so \  
&& POLICY_DIR="UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}" \  
&& curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie" \  
${build_fileserver}/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip >
policy.zip \  
&& unzip policy.zip \  
&& cp -f ${POLICY_DIR}/US_export_policy.jar
${JDK8_HOME}/jre/lib/security/US_export_policy.jar \  
&& cp -f ${POLICY_DIR}/local_policy.jar
${JDK8_HOME}/jre/lib/security/local_policy.jar \  
&& rm -rf ${POLICY_DIR} \  
&& rm -f policy.zip  
  
## install jdk9  
ENV JDK9_HOME /usr/lib/jvm/java-9-oracle  
ENV JRE9_HOME /usr/lib/jvm/java-9-oracle-jre  
RUN echo ===== Install JDK9 ===== \  
&& cd /tmp \  
&& ${ARIA2C_DOWNLOAD} --header="Cookie: oraclelicense=accept-securebackup-
cookie" -d /tmp -o "jdk-9.0.4_linux-x64_bin.tar.gz"
"http://o9wbz99tz.bkt.clouddn.com/otn/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/jdk-9.0.4_linux-x64_bin.tar.gz"
\  
&& tar -xzf jdk-9.0.4_linux-x64_bin.tar.gz \  
&& mkdir -p $(dirname ${JDK9_HOME}) \  
&& mv /tmp/jdk-9.0.4 ${JDK9_HOME} \  
&& rm -f ${JDK9_HOME}/lib/src.zip \  
&& rm -rf /tmp/jdk* \  
&& mkdir -p /Library/Java/JavaVirtualMachines/jdk-9.0.4.jdk/Contents \  
&& ln -s ${JDK9_HOME}
/Library/Java/JavaVirtualMachines/jdk-9.0.4.jdk/Contents/Home \  
&& echo ===== Export jre ===== \  
&& cd $(dirname ${JDK9_HOME}) \  
&& ${JDK9_HOME}/bin/jlink -p ${JDK9_HOME}/jmods --add-modules
java.base,java.sql,java.naming,java.desktop,java.management,java.security.jgss,java.instrument,java.rmi,java.xml.bind,java.xml.ws,java.xml.ws.annotation
--output java-9-oracle-jre \  
&& mkdir -p /Library/Java/JavaVirtualMachines/jre-9.0.4.jre/Contents \  
&& ln -s ${JRE9_HOME}
/Library/Java/JavaVirtualMachines/jre-9.0.4.jre/Contents/Home  
# && ln -s "${JRE9_HOME}/bin/"* "/usr/bin/"  
## install graphviz for maven site javadoc  
RUN apt-get update -y \  
&& apt-get install -y graphviz \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
## install maven && gradle  
RUN MAVEN_VERSION="3.5.3" \  
&& if [ -z "${build_fileserver}" ]; then \  
${ARIA2C_DOWNLOAD} -o apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz; \  
else \  
${ARIA2C_DOWNLOAD} -o apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
${build_fileserver}/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz; \  
fi \  
&& mkdir -p /opt \  
&& tar xf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /opt \  
&& ln -sf /opt/apache-maven-${MAVEN_VERSION} /opt/maven \  
&& rm apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
&& GRADLE_VERSION="4.7" \  
&& if [ -z "${build_fileserver}" ]; then \  
${ARIA2C_DOWNLOAD} -o gradle-${GRADLE_VERSION}-bin.zip
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip; \  
else \  
${ARIA2C_DOWNLOAD} -o gradle-${GRADLE_VERSION}-bin.zip
${build_fileserver}/distributions/gradle-${GRADLE_VERSION}-bin.zip; \  
fi \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip \  
&& mv gradle-${GRADLE_VERSION} /opt \  
&& ln -sf /opt/gradle-${GRADLE_VERSION} /opt/gradle \  
&& rm gradle-${GRADLE_VERSION}-bin.zip  
  
## install rust for current user  
RUN curl -sSf https://sh.rustup.rs > /tmp/install_rustup.sh \  
&& chmod +x /tmp/install_rustup.sh \  
&& /tmp/install_rustup.sh -y \  
&& rm -f /tmp/install_rustup.sh  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV JAVA_HOME ${JDK8_HOME}  
ENV M2_HOME /opt/maven  
ENV GRADLE_HOME /opt/gradle  
ENV JAVA_OPTS -Duser.language=zh -Duser.region=CN -Dfile.encoding='UTF-8'
-Duser.timezone='Asia/Shanghai'  
ENV NODE_HOME /opt/node  
ENV PATH
${JAVA_HOME}/bin:${NODE_HOME}/bin:${M2_HOME}/bin:${GRADLE_HOME}/bin:${PATH}  

