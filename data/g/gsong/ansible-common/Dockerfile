FROM alpine:latest  
ENV PYTHONUNBUFFERED 1  
RUN echo $'source /usr/share/bash-completion/bash_completion\n\  
export HISTFILE=$HOME/.bash_history/history\n\  
PS1=\'\u:\w$ \''\  
>> /etc/bash.bashrc  
  
RUN apk add --update --no-cache \  
bash \  
bash-completion \  
make \  
openssh-client \  
perl \  
py-curl  
  
RUN apk add --update --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/main/ \  
ansible  
  
RUN apk add --update --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
keychain  
  
COPY ./requirements.txt /tmp/  
RUN apk add --update --no-cache \  
gcc \  
musl-dev \  
openssl-dev \  
py-pip \  
python2-dev \  
&& pip install --no-cache-dir -r /tmp/requirements.txt \  
&& apk del \  
gcc \  
musl-dev \  
openssl-dev \  
py-pip \  
python2-dev  
  
WORKDIR /ansible-galaxy/roles  
RUN ansible-galaxy install --roles-path . nickhammond.logrotate  
  
WORKDIR /ansible-common  
COPY playbooks playbooks  
COPY roles roles  
  
WORKDIR /app  

