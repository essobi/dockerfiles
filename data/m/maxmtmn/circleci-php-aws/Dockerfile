FROM circleci/php:7.1.8-browsers  
  
ARG NODE_VERSION  
ENV NODE_VERSION ${NODE_VERSION:-8}  
  
#install php modules for test purposes  
RUN sudo apt-get update && \  
sudo apt-get install -y libpng-dev libmcrypt-dev libmagickwand-dev --no-
install-recommends && \  
sudo docker-php-ext-install gd bcmath mcrypt pdo pdo_mysql zip  
  
#install imagick  
RUN sudo pecl install imagick && sudo docker-php-ext-enable imagick  
  
#install node  
RUN rm -rf ~/.nvm && \  
git clone https://github.com/creationix/nvm.git ~/.nvm && \  
(cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`) && \  
bash -c "source ~/.nvm/nvm.sh && nvm install $NODE_VERSION"  
  
#automatic include of npm  
RUN echo "source /home/circleci/.nvm/nvm.sh" >> /home/circleci/.bashrc  
  
#install gulp, bower  
RUN bash -c "source ~/.nvm/nvm.sh && npm install --global gulp-cli && npm
install --global bower"  
  
#install aws cli  
RUN sudo apt-get install -y python-pip && pip install --user awscli  
  
#install kubectl  
RUN curl -o $HOME/.local/bin/kubectl
https://storage.googleapis.com/kubernetes-
release/release/v1.7.4/bin/linux/amd64/kubectl && \  
chmod +x $HOME/.local/bin/kubectl  
  
RUN echo "export PATH=\$PATH:\$HOME/.local/bin" >> /home/circleci/.bashrc  
  
RUN sudo apt-get remove -y libpng-dev libmcrypt-dev python-pip && sudo apt-get
clean && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#auto auth to aws  
ENTRYPOINT eval $($HOME/.local/bin/aws ecr get-login --region
${AWS_DEFAULT_REGION} \--no-include-email) && /bin/bash  

