FROM xtruder/terraform:0.11.1-goversion  
  
WORKDIR /usr/local/deployer  
  
ADD . /usr/local/deployer  
  
RUN mkdir -p /root/.terraform.d/plugins  
  
RUN git clone https://github.com/xtruder/terraform-provider-mysql.git
$GOPATH/src/github.com/terraform-providers/terraform-provider-mysql  
RUN go get github.com/terraform-providers/terraform-provider-mysql  
RUN go install github.com/terraform-providers/terraform-provider-mysql  
RUN cp $GOPATH/bin/terraform-provider-mysql /root/.terraform.d/plugins  
  
RUN git clone https://github.com/xtruder/terraform-provider-vault.git
$GOPATH/src/github.com/terraform-providers/terraform-provider-vault  
RUN go get github.com/terraform-providers/terraform-provider-vault  
RUN go install github.com/terraform-providers/terraform-provider-vault  
RUN cp $GOPATH/bin/terraform-provider-vault /root/.terraform.d/plugins  
  
RUN git clone https://github.com/xtruder/terraform-provider-kubernetes.git
$GOPATH/src/github.com/terraform-providers/terraform-provider-kubernetes  
RUN go get github.com/terraform-providers/terraform-provider-kubernetes  
RUN go install github.com/terraform-providers/terraform-provider-kubernetes  
RUN cp $GOPATH/bin/terraform-provider-kubernetes /root/.terraform.d/plugins  
  
RUN git clone https://github.com/xtruder/terraform-provider-s3.git
$GOPATH/src/github.com/negronjl/terraform-provider-s3  
RUN go get github.com/negronjl/terraform-provider-s3  
RUN go install github.com/negronjl/terraform-provider-s3  
RUN cp $GOPATH/bin/terraform-provider-s3 /root/.terraform.d/plugins  
  
ENTRYPOINT src/loop.sh  

