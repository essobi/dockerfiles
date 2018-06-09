FROM python:3.6.3-alpine  
# merge https://github.com/yikaus/docker-alpine-bash  
# https://medium.com/@tech_phil/running-ansible-inside-docker-550d3bb2bdff  
# https://github.com/philm/ansible_playbook  
# docker run --rm -it -v $(pwd):/ansible/playbooks philm/ansible_playbook
site.yml  
# docker run --rm -it \  
# -v ~/.ssh/id_rsa:/root/.ssh/id_rsa \  
# -v ~/.ssh/id_rsa.pub:/root/.ssh/id_rsa.pub \  
# -v $(pwd):/ansible/playbooks \  
# philm/ansible_playbook site.yml  
RUN apk --update \  
add --no-cache bash tar curl openssh-client && \  
apk --update add --no-cache --virtual .install_dependencies_paramiko \  
gcc \  
musl-dev \  
python-dev \  
libffi-dev \  
openssl-dev \  
build-base && \  
pip --no-cache-dir install \  
boto python-dateutil httplib2 Jinja2 \  
paramiko pyyaml python-keyczar ansible && \  
apk del .install_dependencies_paramiko && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /etc/ansible/ /ansible  
RUN echo "[local]" >> /etc/ansible/hosts && \  
echo "localhost" >> /etc/ansible/hosts  
  
RUN mkdir -p /ansible/playbooks  
WORKDIR /ansible/playbooks  
  
ENV ANSIBLE_GATHERING smart  
ENV ANSIBLE_HOST_KEY_CHECKING false  
ENV ANSIBLE_RETRY_FILES_ENABLED false  
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles  
ENV ANSIBLE_SSH_PIPELINING True  
  
ENTRYPOINT ["ansible-playbook"]

