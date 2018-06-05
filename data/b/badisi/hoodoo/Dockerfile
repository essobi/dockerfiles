FROM buildpack-deps:jessie  
  
ARG VERSION  
ARG NVM  
ARG NODE  
ARG YARN  
ARG YO  
ARG PLOP  
ARG ELECTRON  
ARG ANGULAR_CLI  
ARG JAVA_MAJOR  
ARG JAVA_MINOR  
ARG JAVA_BUILD  
ARG JAVA_DOWNLOAD_HASH  
ARG MAVEN  
  
# Check for mandatory build arguments  
RUN \  
: "${VERSION:?VERSION argument is required.}" \  
: "${NVM:?NVM argument is required.}" \  
: "${NODE:?NODE argument is required.}" \  
: "${YARN:?YARN argument is required.}" \  
: "${YO:?YO argument is required.}" \  
: "${PLOP:?PLOP argument is required.}" \  
: "${ELECTRON:?ELECTRON argument is required.}" \  
: "${ANGULAR_CLI:?ANGULAR_CLI argument is required.}" \  
: "${JAVA_MAJOR:?JAVA_MAJOR argument is required.}" \  
: "${JAVA_MINOR:?JAVA_MINOR argument is required.}" \  
: "${JAVA_BUILD:?JAVA_BUILD argument is required.}" \  
: "${JAVA_DOWNLOAD_HASH:?JAVA_DOWNLOAD_HASH argument is required.}" \  
: "${MAVEN:?MAVEN argument is required.}"  
  
LABEL name="hoodoo" \  
version=${VERSION} \  
maintainer="badisi"  
  
ENV USER hoodoo  
ENV USER_DIR /home/$USER  
ENV WORK_DIR=$USER_DIR/workspace \  
NVM_DIR=$USER_DIR/.nvm \  
IMAGE_VERSION=${VERSION}  
  
# Install updates and essential packages  
RUN set -ex \  
&& apt-get update && apt-get install -y software-properties-common build-
essential sudo git \  
  
# Install graphic packages  
&& apt-get update && apt-get install -y libgtk2.0-0 libx11-xcb1 libxtst6
libxss1 libgconf-2-4 libnss3 libasound2 \  
  
# Install java  
&& mkdir -p /usr/lib/jvm \  
&& wget -nv -P /tmp --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR}u${JAVA_MINOR}-b${JAVA_BUILD}/${JAVA_DOWNLOAD_HASH}/jdk-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz
\  
&& tar xzvf /tmp/jdk-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz -C
/usr/lib/jvm \  
&& update-alternatives --install "/usr/bin/java" "java"
"/usr/lib/jvm/jdk1.${JAVA_MAJOR}.0_${JAVA_MINOR}/bin/java" 1 \  
  
# Install maven  
&& mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz
https://apache.osuosl.org/maven/maven-3/${MAVEN}/binaries/apache-
maven-${MAVEN}-bin.tar.gz \  
&& tar xzvf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
  
# Clean  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create our user and use it from now on  
RUN adduser --disabled-password --gecos "" $USER; \  
echo "$USER ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers;  
USER $USER  
# Install nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v${NVM}/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
  
# Install node  
&& nvm install ${NODE} \  
&& nvm alias default ${NODE} \  
&& nvm use default \  
  
# Install yarn + dependencies  
&& curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version ${YARN} \  
&& $HOME/.yarn/bin/yarn global add \  
yo@${YO} \  
plop@${PLOP} \  
electron@${ELECTRON} \  
@angular/cli@${ANGULAR_CLI} \  
  
# Create working directory  
&& mkdir -p $WORK_DIR  
  
WORKDIR $WORK_DIR  
CMD ["bash"]  

