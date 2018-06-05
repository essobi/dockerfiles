FROM hashicorp/terraform:0.8.1  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
ENV TERRAFORM_ARUKAS_VERSION=0.1.0  
ADD https://github.com/yamamoto-febc/terraform-provider-
arukas/releases/download/v${TERRAFORM_ARUKAS_VERSION}/terraform-provider-
arukas_linux-amd64.zip ./  
RUN unzip terraform-provider-arukas_linux-amd64.zip -d /bin  
RUN rm -f terraform-provider-arukas_linux-amd64.zip  
  
VOLUME ["/work"]  
WORKDIR /work  
  
ENTRYPOINT ["/bin/terraform"]  
CMD ["--help"]  

