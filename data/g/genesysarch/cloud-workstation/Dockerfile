#Build directory: None  
#tag: cloud-workstation  
FROM gliderlabs/alpine:3.3  
#Commands for devbase  
RUN apk add --update --no-cache \  
ca-certificates curl wget make bash openssh-client \  
bash git sshpass rsync  
  
#Commands for python  
RUN apk add --update --no-cache python \  
python-dev \  
py-pip \  
&& pip install virtualenv docopts \  
&& rm -rf /var/cache/apk/* \  
&& pip install --upgrade pip  
  
#Commands for awscli  
RUN pip install awscli  
COPY build/aws/aws_bash_helpers.sh /root/.bashrc  
  
#Commands for terraform  
ARG TERRAFORM_VERSION=0.8.5  
RUN wget -P /tmp
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
&& \  
unzip /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
RUN wget -P /tmp
https://github.com/CiscoCloud/terraform.py/blob/master/terraform.py && \  
mv /tmp/terraform.py /usr/local/bin && chmod 755 /usr/local/bin/terraform.py  
  
#Commands for ansible  
ARG TERRAFORM_INVENTORY_VERSION=v0.6.1  
ENV PATH /ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/bin  
ENV PYTHONPATH /ansible/lib  
ENV ANSIBLE_LIBRARY /ansible/library  
  
RUN apk --no-cache add --update -t deps git gcc make musl-dev libxml2-dev \  
libxslt-dev openssl-dev libffi-dev  
RUN pip install ansible ansible-vault  
  
RUN mkdir -p $ANSIBLE_LIBRARY && wget https://github.com/adammck/terraform-
inventory/releases/download/$TERRAFORM_INVENTORY_VERSION/terraform-
inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip \  
&& unzip terraform-inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip \  
&& chmod 755 terraform-inventory && mv terraform-inventory $ANSIBLE_LIBRARY/
&& rm terraform-inventory_${TERRAFORM_INVENTORY_VERSION}_linux_amd64.zip  
RUN apk del --purge deps;  
  
#Commands for testing  
RUN git clone https://github.com/calj/bats.git && bats/install.sh /usr/local \  
&& rm -rf bats  
  
#Commands for dockerize  
ENV DOCKERIZE_VERSION v0.3.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
#Commands for direnv  
ENV DIRENV_VERSION v2.11.3  
RUN wget -O direnv
https://github.com/direnv/direnv/releases/download/$DIRENV_VERSION/direnv.linux-
amd64
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& chmod 755 direnv && mv direnv /usr/local/bin  
COPY build/direnv/direnv_helpers.sh /root/.bashrc  
  
#Commands for clitools  
COPY ./build/scripts/* /usr/local/bin/  
COPY ./build/templates /opt/cloud-workstation/templates  
RUN chmod 755 /usr/local/bin/*  
  
#Commands for cloud-workstation  
WORKDIR /workspace  
CMD /bin/bash  
  

