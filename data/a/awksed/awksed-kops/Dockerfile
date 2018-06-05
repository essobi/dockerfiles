FROM python  
LABEL maintainer="michael@hayslip.info"  
  
RUN apt-get update  
RUN apt-get install -y wget iputils-ping net-tools dnsutils vim  
RUN pip install awscli  
  
VOLUME [ "/root/kops" ]  
  
# Install kubectl  
RUN wget -O kubectl https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
  
# Install kops  
RUN curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s
https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name |
cut -d '"' -f 4)/kops-linux-amd64  
RUN chmod +x kops-linux-amd64  
RUN mv kops-linux-amd64 /usr/local/bin/kops  
  
CMD [ "bash" ]  

