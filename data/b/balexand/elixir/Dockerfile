FROM elixir:1.6.5  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update  
RUN apt-get install -y build-essential lsb-release netcat nodejs postgresql-
client sudo yarn  
  
RUN curl -fSL -o /root/docker.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-17.09.0-ce.tgz  
RUN cd /root && tar xzf docker.tgz  
RUN cp /root/docker/* /usr/bin/  
  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key
add -  
RUN apt-get update  
RUN apt-get install -y google-cloud-sdk  
RUN gcloud config set core/disable_usage_reporting true  
RUN gcloud config set component_manager/disable_update_check true  
RUN gcloud config set metrics/environment github_docker_image  

