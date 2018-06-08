FROM gamestop/gs.docker.buildenv.ubuntu:14.04  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/v1.9.1/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& sudo mv ./kubectl /usr/local/bin/kubectl  
  
RUN echo 'alias k="kubectl"' >> ~/.bashrc  

