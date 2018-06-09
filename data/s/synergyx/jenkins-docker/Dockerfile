FROM jenkins  
USER root  
RUN apt-get update \  
&& apt-get install -y sudo vim \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-get update && apt-get install -y libltdl7 && rm -rf
/var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN wget -O kops https://github.com/kubernetes/kops/releases/download/$(curl
-s https://api.github.com/repos/kubernetes/kops/releases/latest | grep
tag_name | cut -d '"' -f 4)/kops-linux-amd64  
RUN chmod +x ./kops  
RUN mv ./kops /usr/local/bin/  
  
RUN wget -O kubectl https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
  
EXPOSE 8080  

