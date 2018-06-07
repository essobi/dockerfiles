FROM hootsuite/atlantis  
  
RUN curl -LOk
https://releases.hashicorp.com/terraform/0.10.8/terraform_0.10.8_linux_amd64.zip  
  
RUN apk add unzip  
  
RUN mkdir -p /usr/local/bin/tf/versions/0.10.8  
RUN unzip terraform_0.10.8_linux_amd64.zip -d
/usr/local/bin/tf/versions/0.10.8  
RUN ln -s /usr/local/bin/tf/versions/0.10.8/terraform
/usr/local/bin/terraform0.10.8;rm terraform_0.10.8_linux_amd64.zip && \  
rm /usr/local/bin/terraform && ln -s
/usr/local/bin/tf/versions/0.10.8/terraform /usr/local/bin/terraform  

