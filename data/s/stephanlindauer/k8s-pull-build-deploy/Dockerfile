FROM ruby:2.2  
RUN apt-get -qq update && \  
apt-get -qq -y install curl git-core jq  
  
# install kubectl  
RUN curl -O https://storage.googleapis.com/kubernetes-
release/release/v1.4.3/bin/linux/amd64/kubectl && \  
mv kubectl /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl  
  
WORKDIR /home  
  
# install app  
ADD ./Gemfile* /k8s-pull-build-deploy/  
WORKDIR /k8s-pull-build-deploy/  
RUN bundle install  
  
ADD . /k8s-pull-build-deploy  
  
CMD ruby run.rb  

