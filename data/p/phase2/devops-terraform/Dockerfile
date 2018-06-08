FROM phase2/alpine:3.4  
ENV TERRAFORM_VERSION=0.7.2 \  
TERRAFORM_DEPS="openssh-client"  
RUN apk --no-cache add ${TERRAFORM_DEPS} && \  
/installers/terraform.sh  
  
WORKDIR /code  
  
ENTRYPOINT [ "/usr/local/bin/terraform" ]  

