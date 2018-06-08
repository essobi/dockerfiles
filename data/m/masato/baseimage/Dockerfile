FROM phusion/baseimage:0.9.15  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV RUBY_VERSION 2.2.0  
ENV TYPESAFE_VERSION 1.2.10  
ENV NODE_VERSION v0.10  
ENV LEIN_VERSION 2.5.0  
# Set correct environment variables.  
ENV HOME /root  
  
# Regenerate SSH host keys.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
## Enabling the insecure key permanently  
RUN /usr/sbin/enable_insecure_key  
  
## apt-get update  
RUN add-apt-repository ppa:webupd8team/java && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y build-essential software-properties-common \  
autoconf bison build-essential libssl-dev libyaml-dev \  
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev \  
zlib1g-dev libyaml-dev \  
libxml2-dev libxslt-dev sqlite3 libsqlite3-dev \  
emacs24-nox emacs24-el git byobu wget curl unzip tree elinks \  
python-dev python-pip golang \  
oracle-java8-installer oracle-java8-set-default ant maven  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
## Japanese Environment  
ENV LANG ja_JP.UTF-8  
RUN locale-gen $LANG && update-locale $LANG && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
## Development Environment  
RUN update-alternatives --set editor /usr/bin/vim.basic  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
ENV PATH $PATH:${HOME}/bin  
  
# Add Un-Root User  
RUN useradd -m -d ${HOME} -s /bin/bash ${USERNAME} && \  
echo "${USERNAME}:${USERNAME}" | chpasswd && \  
mkdir ${HOME}/.ssh ${HOME}/tmp && \  
chmod 700 ${HOME}/.ssh && \  
cp /root/.ssh/authorized_keys ${HOME}/.ssh && \  
chmod 600 ${HOME}/.ssh/authorized_keys && \  
chown -R ${USERNAME}:${USERNAME} ${HOME}/.ssh && \  
echo "export LANG=ja_JP.UTF-8" >> ${HOME}/.bashrc && \  
echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
## Ruby ruby-build install  
RUN git clone https://github.com/sstephenson/ruby-build.git .ruby-build && \  
.ruby-build/install.sh && \  
rm -fr .ruby-build && \  
ruby-build ${RUBY_VERSION} /usr/local && \  
gem update --system && \  
gem install bundler --no-rdoc --no-ri  
  
## Mono/F#  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mono-devel fsharp mono-vbnc
nuget  
  
RUN mozroots --machine --import --sync --quiet  
  
ENV USERNAME docker  
ENV HOME /home/${USERNAME}  
  
ADD dotfiles ${HOME}  
RUN chown -R ${USERNAME}:${USERNAME} ${HOME}  
  
USER ${USERNAME}  
WORKDIR ${HOME}  
  
## Node.js/StrongLoop  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.22.0/install.sh |
bash && \  
/bin/bash -c 'source ${HOME}/.nvm/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias default ${NODE_VERSION} && \  
npm install -g npm && \  
npm install -g strongloop && \  
npm install -g jsxhint && \  
npm cache clear'  
  
## Go  
RUN mkdir -p ${HOME}/gocode/src ${HOME}/gocode/bin ${HOME}/gocode/pkg && \  
echo "export GOPATH=${HOME}/gocode" >> ${HOME}/.bashrc && \  
echo "export PATH=${PATH}:${HOME}/gocode/bin" >> ${HOME}/.bashrc  
  
## Dart  
RUN wget http://storage.googleapis.com/dart-
archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip -P
${HOME} && \  
unzip ${HOME}/dartsdk-linux-x64-release.zip -d ${HOME} && \  
echo "export PATH=${PATH}:${HOME}/dart-sdk/bin" >> ${HOME}/.bashrc && \  
rm ${HOME}/dartsdk-linux-x64-release.zip  
  
## Scala  
RUN mkdir -p ${HOME}/bin && \  
wget http://downloads.typesafe.com/typesafe-
activator/${TYPESAFE_VERSION}/typesafe-activator-${TYPESAFE_VERSION}.zip -P
${HOME} && \  
unzip ${HOME}/typesafe-activator-${TYPESAFE_VERSION}.zip -d ${HOME} && \  
ln -s ${HOME}/activator-${TYPESAFE_VERSION}/activator ${HOME}/bin/activator &&
\  
rm ${HOME}/typesafe-activator-${TYPESAFE_VERSION}.zip  
  
## Cask  
RUN curl -fsSkL https://raw.github.com/cask/cask/master/go | python && \  
echo "export PATH=${HOME}/.cask/bin:$PATH" >> ${HOME}/.profile && \  
/bin/bash -c "source ${HOME}/.profile && cd ${HOME}/.emacs.d && cask install"  
  
## Clojure  
RUN curl -s
https://raw.githubusercontent.com/technomancy/leiningen/${LEIN_VERSION}/bin/lein
> \  
${HOME}/bin/lein && \  
chmod 0755 ${HOME}/bin/lein  
ENV LEIN_ROOT 1  
RUN lein  
  
ADD dotfiles/.lein/profiles.clj ${HOME}/.lein/  
  
## Groovy/Spring Boot/Gradle  
RUN curl -s get.gvmtool.net | bash && \  
/bin/bash -c 'source ${HOME}/.gvm/bin/gvm-init.sh && gvm install springboot &&
gvm install gradle'  
  
## auto-java-complete  
RUN cd ${HOME}/.emacs.d && \  
git clone https://github.com/emacs-java/auto-java-complete && \  
cd auto-java-complete && \  
javac Tags.java -encoding UTF-8 && \  
java -cp "/usr/lib/jvm/java-8-oracle/jre/lib/rt.jar:." Tags  
  
USER root  
ENV HOME /root  
WORKDIR /root  
  
ADD sv /etc/service  
CMD ["/sbin/my_init"]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

