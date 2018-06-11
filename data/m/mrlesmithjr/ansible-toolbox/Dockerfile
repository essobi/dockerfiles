FROM alpine  
  
MAINTAINER Larry Smith Jr.  
  
RUN apk --update add bash git python py2-pip openssl ca-certificates sshpass \  
openssh-client sudo && \  
apk add --virtual build-dependencies \  
python-dev libffi-dev openssl-dev build-base && \  
pip install --upgrade pip cffi  
  
RUN addgroup ansible && \  
adduser -G ansible -g "Ansible User" -s /bin/bash -D ansible && \  
echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
COPY setup_python_virtualenvs.sh /home/ansible/setup_python_virtualenvs.sh  
  
RUN pip install virtualenv  
  
RUN mkdir -p /home/ansible/ansible /home/ansible/python-virtualenvs && \  
chmod 0777 /home/ansible/ansible /home/ansible/python-virtualenvs  
  
RUN su ansible -c "/home/ansible/setup_python_virtualenvs.sh"  
  
RUN apk del build-dependencies && \  
rm -rf /var/cache/apk/*  
  
USER ansible  
  
WORKDIR /home/ansible  
  
VOLUME ["/home/ansible/.ssh", "/home/ansible/ansible", "/home/ansible/python-
virtualenvs"]  
  
CMD ["sh"]  

