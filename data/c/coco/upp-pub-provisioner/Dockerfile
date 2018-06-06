FROM alpine  
  
RUN echo "[localhost]" > ~/.ansible_hosts \  
&& echo '127.0.0.1 ansible_python_interpreter=/.venv/bin/python' >>
~/.ansible_hosts \  
&& apk --update add py-pip py-virtualenv gcc python-dev libffi-dev openssl-dev
build-base bash jq util-linux curl \  
&& mkdir .venv \  
&& virtualenv .venv \  
&& . .venv/bin/activate \  
&& pip install ansible==2.0.2.0 boto awscli  
  
ADD *.sh /  
ADD cluster-id-extractor /  
ADD ansible/ /ansible  
  
RUN ln -s /cluster-id-extractor /usr/local/bin/cluster-id-extractor  
  
CMD /bin/bash provision.sh  

