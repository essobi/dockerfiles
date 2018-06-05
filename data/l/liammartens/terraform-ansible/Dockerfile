FROM alpine:3.7 as builder  
  
# @arg terraform version  
ARG TERRAFORM_VERSION=0.11.3  
  
# @arg define ops user  
ARG USER=ops  
  
# @run update and upgrade  
RUN apk update && apk upgrade  
  
# @run add unzip  
RUN apk add python3 ca-certificates python3-dev unzip alpine-sdk libffi-dev
openssl-dev && \  
ln -s /usr/bin/python3 /usr/bin/python  
  
# @run install terraform  
RUN curl -L
"https://releases.hashicorp.com/terraform/0.11.3/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"
-o terraform.zip && \  
unzip terraform.zip && rm terraform.zip && mv terraform /usr/bin/terraform  
  
# @run install ansible  
RUN pip3 install ansible  
  
# @run remove packages  
RUN apk del python3-dev alpine-sdk libffi-dev openssl-dev unzip  
  
# @add localhost to ansible hosts  
RUN mkdir /etc/ansible && \  
echo "[local]" > /etc/ansible/hosts && \  
echo "localhost ansible_connection=local" >> /etc/ansible/hosts  
  
# @run add devops user  
RUN adduser -D ${USER}  
# @user switch to ops user  
USER ${USER}  
# @workdir Set workdir to home  
WORKDIR /home/${USER}  
# @volume Define volume  
VOLUME /home/${USER}  
# @entrypoint define terraform as default entrypoint (ansible should be run
from within terraform)  
ENTRYPOINT [ "terraform" ]  
  
# @cmd set help  
CMD [ "--help" ]

