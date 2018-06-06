FROM alpine  
LABEL maintainer="KOJIMA Kazunori kjm.kznr@gmail.com"  
  
ENV TERRAFORM_VERSION=0.11.7  
RUN apk --update add git bash bzr git mercurial subversion openssh-client ca-
certificates curl  
RUN curl -LOs
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin/  
RUN rm -rf /var/cache/apk/* terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
  
CMD ["/usr/bin/terraform"]  

