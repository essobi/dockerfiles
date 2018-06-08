FROM python  
  
RUN pip install ansible apache-libcloud  
  
RUN apt-get update && apt-get install -y --no-install-recommends unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TERRAFORM_VERSION 0.11.7  
RUN curl -sSL -O
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
\  
&& unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip \  
&& mv terraform /usr/local/bin  

