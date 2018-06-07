FROM debian:latest  
RUN apt update && apt -y install python3-pip && pip3 install yamllint  
ADD https://github.com/garethr/kubeval/releases/download/0.7.1/kubeval-linux-
amd64.tar.gz /kubeval-linux-amd64.tar.gz  
RUN tar -C /usr/local/bin -xf /kubeval-linux-amd64.tar.gz && rm /kubeval-
linux-amd64.tar.gz  
ADD https://github.com/garethr/kubetest/releases/download/0.1.1/kubetest-
linux-amd64.tar.gz /kubetest-linux-amd64.tar.gz  
RUN tar -C /usr/local/bin -xf /kubetest-linux-amd64.tar.gz  

