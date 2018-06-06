  
FROM cirepo/ci-ubuntu:18.04  
# ------------------------------ evarga/jenkins-slave
------------------------------  
# ------------------------------ evarga/jenkins-slave
------------------------------  
# ------------------------------ carlossg/jenkins-swarm-slave
------------------------------  
ENV JENKINS_SWARM_VERSION 3.12  
ENV HOME /home/jenkins-slave  
  
# install netstat to allow connection health check with  
# netstat -tan | grep ESTABLISHED  
RUN sed -i
's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.163.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y net-tools curl iputils-ping zip unzip \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
RUN useradd -c "Jenkins Slave user" -d $HOME -m jenkins-slave  
RUN curl --create-dirs -sSLo /usr/share/jenkins/swarm-
client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar \  
https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-
client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar \  
&& chmod 755 /usr/share/jenkins  
  
RUN gpasswd -a jenkins-slave docker  
USER jenkins-slave  
RUN mkdir -p /home/jenkins-slave/.m2  
RUN mkdir -p /home/jenkins-slave/.ssh  
VOLUME /home/jenkins-slave  
  
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
# ------------------------------ carlossg/jenkins-swarm-slave
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

