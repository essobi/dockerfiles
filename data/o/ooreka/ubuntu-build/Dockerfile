FROM ubuntu:latest  
  
RUN apt-get update && apt-get install git jq unzip curl -y  
RUN git clone https://github.com/kamatama41/tfenv.git ~/.tfenv && \  
echo 'export PATH="$HOME/.tfenv/bin:$PATH"' >> ~/.bashrc  
  
RUN curl
https://releases.hashicorp.com/packer/1.1.3/packer_1.1.3_linux_amd64.zip >
packer.zip && \  
unzip packer.zip && \  
mv packer /usr/bin/  
  
RUN curl
https://releases.hashicorp.com/terraform/0.11.1/terraform_0.11.1_linux_amd64.zip
> terraform.zip && \  
unzip terraform.zip && \  
mv terraform /usr/bin/  

