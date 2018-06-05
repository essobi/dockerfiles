FROM gradle:4.5.1-jdk8  
  
USER root  
  
# Install jfrog client  
RUN curl -fL https://getcli.jfrog.io | sh && \  
mv jfrog /usr/local/bin && \  
chmod a+x /usr/local/bin/jfrog  
  
RUN wget
https://releases.hashicorp.com/packer/1.2.1/packer_1.2.1_linux_amd64.zip && \  
unzip packer_1.2.1_linux_amd64.zip && \  
mv packer /usr/local/bin && \  
chmod a+x /usr/local/bin/packer  
  
ENV TERRAFORM_VERSION=0.11.7  
ADD
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
/tmp/terraform.zip  
RUN cd /usr/local/bin \  
&& unzip /tmp/terraform.zip \  
&& chmod +x /usr/local/bin/terraform \  
&& rm /tmp/terraform.zip  
  
USER gradle  

