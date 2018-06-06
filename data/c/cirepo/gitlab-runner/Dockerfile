  
FROM cirepo/ci-ubuntu:18.04  
#wget -q -O - https://packages.gitlab.com/gpg.key | apt-key add - \  
# then  
#echo "deb https://packages.gitlab.com/runner/gitlab-ci-multi-runner/ubuntu/
bionic main" > /etc/apt/sources.list.d/runner_gitlab-ci-multi-runner.list &&
apt-get update -y  
# or  
#add-apt-repository "deb https://packages.gitlab.com/runner/gitlab-ci-multi-
runner/ubuntu/ $(lsb_release -cs) main" -u  
RUN ${ARIA2C_DOWNLOAD} -d /usr/bin -o dumb-init "https://github.com/Yelp/dumb-
init/releases/download/v1.2.1/dumb-init_1.2.1_amd64" \  
&& chmod +x /usr/bin/dumb-init \  
&& apt-get update -y \  
&& apt-cache madison gitlab-runner \  
&& apt-get install -yq sudo gitlab-runner=10.5.0+dfsg-2 \  
&& mkdir -p /etc/gitlab-runner/certs \  
&& chmod -R 700 /etc/gitlab-runner \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Set environment variables, add user gitlab-runner into docker group, fix
Directory permissions.  
RUN echo '\nexport JAVA_HOME=/opt/jdk\n\  
export M2_HOME=/opt/maven\n\  
export NODE_HOME=/opt/node\n\  
export GRADLE_HOME=/opt/gradle\n\n\  
export
PATH=$JAVA_HOME/bin:$NODE_HOME/bin:$GRADLE_HOME/bin:$M2_HOME/bin:$PATH\n' >>
/etc/profile \  
&& gpasswd -a gitlab-runner docker \  
&& echo "gitlab-runner ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& chown -R gitlab-runner:docker /opt/node-*/lib \  
&& chown -R gitlab-runner:docker /opt/node-*/bin \  
&& mkdir -p /home/gitlab-runner \  
&& chown -R gitlab-runner:docker /home/gitlab-runner \  
&& chown -R gitlab-runner:docker /var/lib/gitlab-runner  
  
ADD docker/entrypoint /  
RUN chmod +x /entrypoint  
  
VOLUME ["/etc/gitlab-runner", "/var/lib/gitlab-runner"]  
  
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/var/lib/gitlab-
runner"]  
  
  
USER gitlab-runner  
  
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
&& /bin/bash \--login -c "pyenv install 2.7.14 && pyenv install 3.6.5" \  
## install rust for current user  
RUN curl -sSf https://sh.rustup.rs > /tmp/install_rustup.sh \  
&& chmod +x /tmp/install_rustup.sh \  
&& /tmp/install_rustup.sh -y \  
&& rm -f /tmp/install_rustup.sh  

