FROM gitlab/gitlab-runner:ubuntu-v10.1.0  
# Install docker  
RUN sudo curl -sSL https://get.docker.com/ | sh \  
&& sudo usermod -aG docker gitlab-runner  
  
COPY docker-entrypoint /  
  
# Install nodejs, npm  
RUN wget -q -O - https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& sudo apt-get install nodejs -y \  
&& node --version  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list \  
&& sudo apt-get update && sudo apt-get install -y yarn \  
&& yarn --version  
  
# Install jest and lerna  
RUN yarn global add jest lerna  
  
# Install helm  
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get
> get_helm.sh \  
&& chmod 700 get_helm.sh \  
&& ./get_helm.sh \  
&& helm init --client-only  
  
ENTRYPOINT ["/usr/bin/dumb-init","/docker-entrypoint"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  

