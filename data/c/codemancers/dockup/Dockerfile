FROM elixir:1.5.1  
RUN apt-get update  
RUN wget -qO- https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get update && apt-get install -y nodejs build-essential  
  
# https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl  
RUN apt-get update && apt-get install -y apt-transport-https  
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key
add -  
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" >
/etc/apt/sources.list.d/kubernetes.list  
RUN apt-get update && apt-get install -y kubectl  
  
# https://docs.helm.sh/using_helm/#installing-helm  
RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v2.9.1-linux-
amd64.tar.gz  
RUN tar xzvf helm-v2.9.1-linux-amd64.tar.gz && cp /linux-amd64/helm
/usr/local/bin/helm  
  
# Install docker and docker-compose  
#RUN curl -sSL https://get.docker.com/ | sh  
#RUN sh -c "curl -L
https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"  
#RUN chmod +x /usr/local/bin/docker-compose  
RUN mkdir -p /dockup  
WORKDIR /dockup  
COPY . ./  
COPY ./apps/dockup_ui/config/prod.secret.example.exs
apps/dockup_ui/config/prod.secret.exs  
  
ENV MIX_ENV prod  
ENV PORT 4000  
RUN mix local.hex --force  
RUN mix local.rebar --force  
RUN mix deps.get --force --only prod  
RUN mix compile  
  
# Precompile DockupUi assets  
WORKDIR /dockup/apps/dockup_ui  
RUN npm install  
RUN ./node_modules/brunch/bin/brunch build --production  
RUN mix phoenix.digest  
  
WORKDIR /dockup  
EXPOSE 4000  
CMD ./scripts/run  

