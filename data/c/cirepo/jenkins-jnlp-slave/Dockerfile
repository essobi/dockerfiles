  
FROM cirepo/ci-ubuntu:18.04  
# install netstat to allow connection health check with  
# netstat -tan | grep ESTABLISHED  
RUN sed -i
's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update -y \  
&& apt-get install -y net-tools curl \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
# ------------------------------ jenkinsci/docker-slave
------------------------------  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=10000  
ARG gid=10000  
ENV HOME /home/${user}  
RUN groupadd -g ${gid} ${group}  
RUN useradd -c "Jenkins user" -d $HOME -u ${uid} -g ${gid} -m ${user}  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar)" Vendor="Jenkins project" Version="3.20"  
  
ARG VERSION=3.20  
ARG AGENT_WORKDIR=/home/${user}/agent  
  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
USER ${user}  
ENV AGENT_WORKDIR=${AGENT_WORKDIR}  
RUN mkdir /home/${user}/.jenkins && mkdir -p ${AGENT_WORKDIR}  
  
VOLUME /home/${user}/.jenkins  
VOLUME ${AGENT_WORKDIR}  
WORKDIR /home/${user}  
  
# ------------------------------ jenkinsci/docker-slave
------------------------------  
# ------------------------------ jenkinsci/jnlp-slave
------------------------------  
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
# ------------------------------ jenkinsci/jnlp-slave
------------------------------  
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
## install python for current user  
RUN set -ex \  
&& curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-
installer | bash \  
&& touch ~/.bash_profile \  
&& echo 'export PATH="${HOME}/.pyenv/bin:$PATH"' >> ~/.bash_profile \  
&& echo 'if which pyenv > /dev/null; then eval "$(pyenv init -)"; eval
"$(pyenv virtualenv-init -)"; fi' >> ~/.bash_profile \  
&& /bin/bash --login -c "pyenv install 2.7.14 && pyenv install 3.6.5" \  
## install rust for current user  
RUN curl -sSf https://sh.rustup.rs > /tmp/install_rustup.sh \  
&& chmod +x /tmp/install_rustup.sh \  
&& /tmp/install_rustup.sh -y \  
&& rm -f /tmp/install_rustup.sh  

