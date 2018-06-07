#Build directory: None  
#tag: cloud-workstation  
FROM python:3-alpine as base  
RUN apk add --update --no-cache \  
ca-certificates curl wget openssh-client bash git jq \  
make git  
  
FROM base as terraform  
ARG TERRAFORM_VERSION=0.11.3  
RUN wget -P /tmp
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin &&
\  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ARG TERRAGRUNT_VERSION=v0.13.23  
RUN wget -O terragrunt https://github.com/gruntwork-
io/terragrunt/releases/download/$TERRAGRUNT_VERSION/terragrunt_linux_amd64 \  
&& chmod 755 terragrunt && mv terragrunt /usr/local/bin  
  
ARG TERAFORM_DOCS=v0.3.0  
RUN wget -O terraform-docs https://github.com/segmentio/terraform-
docs/releases/download/$TERAFORM_DOCS/terraform-docs_linux_amd64 \  
&& chmod 755 terraform-docs && mv terraform-docs /usr/local/bin/terraform-docs  
  
# Preload terraform plugins  
COPY /terrasetup/terraformrc /root/.terraformrc  
COPY /terrasetup/* /tmp/terraform/  
RUN cd /tmp/terraform && terragrunt init  
  
FROM python:3-alpine as python-base  
RUN pip install virtualenv  
RUN virtualenv /opt/workstation/py  
  
FROM python-base as pytools  
COPY requirements.txt .  
RUN apk add --update --no-cache bash  
# Need build tools  
RUN apk --no-cache add --update -t deps git gcc make musl-dev libxml2-dev \  
libxslt-dev openssl-dev libffi-dev linux-headers  
# virtualenv must be sourced which is a bash function  
RUN /bin/bash -c 'source /opt/workstation/py/bin/activate && pip install -r
requirements.txt'  
  
FROM base as ecs  
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest  
RUN chmod 755 /usr/local/bin/ecs-cli  
  
FROM base as direnv  
ARG DIRENV_VERSION=v2.13.1  
RUN wget -P /tmp
https://github.com/direnv/direnv/releases/download/${DIRENV_VERSION}/direnv.linux-
amd64  
RUN mv /tmp/direnv.linux-amd64 /usr/local/bin/direnv && chmod 755
/usr/local/bin/direnv  
  
# TODO this is the one part that is organization specific, consider moving to
separate Dockerfile  
FROM base as docker  
ARG DOCKER_BUCKET=get.docker.com  
ARG DOCKER_VERSION=1.9.1  
RUN curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION" -o
/usr/local/bin/docker \  
&& chmod +x /usr/local/bin/docker  
  
  
FROM base  
COPY \--from=ecs /usr/local/bin/ecs-cli /usr/local/bin  
COPY \--from=terraform /usr/local/bin/terra* /usr/local/bin/  
COPY \--from=pytools /opt/workstation/py /opt/workstation/py  
COPY \--from=direnv /usr/local/bin/direnv /usr/local/bin  
COPY \--from=terraform /root/.terraformrc /root/.terraformrc  
COPY \--from=terraform /root/.terraform.d/* /root/.terraform.d/  
COPY \--from=docker /usr/local/bin/docker /usr/local/bin/  
  
COPY bash_profile_helpers/* /etc/profile.d/  
RUN chmod 755 /usr/local/bin/*  
  
ENV TERRAFORM_CACHE_DIR /root/.terraform.d/linux_amd64  
WORKDIR /workspace  
ENTRYPOINT ["/bin/bash", "-login"]  
  

