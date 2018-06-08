FROM alpine:latest  
MAINTAINER "Jonatan Bjork <jonatan@jonatanblue.se>"  
  
ARG TERRAFORM_VERSION=0.9.11  
ARG
TERRAFORM_SHA256SUM=804d31cfa5fee5c2b1bff7816b64f0e26b1d766ac347c67091adccc2626e16f3  
  
ENV TERRAFORM_FILENAME=terraform_${TERRAFORM_VERSION}_linux_amd64.zip  
ENV
TERRAFORM_URL=https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/${TERRAFORM_FILENAME}  
RUN apk add \--update git bash wget  
  
RUN wget -q ${TERRAFORM_URL} \  
&& echo "${TERRAFORM_SHA256SUM} ${TERRAFORM_FILENAME}" | sha256sum -c  
RUN unzip ${TERRAFORM_FILENAME} -d /bin  
RUN rm -f ${TERRAFORM_FILENAME}  

