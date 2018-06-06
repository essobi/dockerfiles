FROM golang:stretch  
  
# Add in helper file(s).  
COPY files/ /  
  
# Set up software.  
RUN apt-get update  
RUN apt-get install -y awscli curl gcc git jq make tar unzip wget  
  
# Set up packer and terraform.  
WORKDIR /usr/local/bin  
RUN wget -q
"https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip"  
RUN wget -q
"https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip"  
RUN unzip '*.zip' && rm *.zip  
RUN chmod +x packer terraform  
  
# Install gometalinter.  
RUN go get -u github.com/alecthomas/gometalinter  
RUN $GOPATH/bin/gometalinter --install  
  
# Install go dep.  
RUN go get -u github.com/golang/dep/cmd/dep  

