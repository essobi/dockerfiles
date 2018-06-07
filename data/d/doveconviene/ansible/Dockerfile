FROM alpine:latest  
MAINTAINER ShopfullyGroup <server@doveconviene.com>  
RUN apk add --update --no-cache --virtual build-dependencies \  
python openssh-client git rsync openssl ca-certificates python-dev libffi-dev
openssl-dev build-base && \  
python -m ensurepip && \  
pip install --upgrade pip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade cffi && \  
pip install --upgrade ansible Jinja2 ansible-lint && \  
pip install --upgrade awscli boto3 ec2 && \  
pip install --upgrade pyvmomi pysphere && \  
pip install --upgrade dopy && \  
pip install --upgrade docker-py && \  
rm -r /root/.cache && \  
export PATH=~/.local/bin:$PATH  
  
ENV PATH /root/.local/bin:$PATH  
ENTRYPOINT ["ansible-playbook"]  
VOLUME ["/etc/ansible", "/root/.aws", "/root/.ssh", "/var/run/docker.sock",
"/root/.ssh", "/root/vault-pass.txt"]  
WORKDIR /etc/ansible  

