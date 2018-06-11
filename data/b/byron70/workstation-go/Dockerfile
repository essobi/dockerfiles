FROM golang:1.8.3-alpine3.6  
ENV PATH /usr/local/bin:$PATH  
ENV LANG C.UTF-8  
RUN set -eux  
RUN apk add --no-cache ca-certificates alpine-sdk docker \  
zip nmap nano tar openssl openssl-dev \  
bash bash-completion curl wget jq \  
python3 python3-dev python2-dev libffi-dev libc-dev linux-headers openssh \  
bind-tools coreutils  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
wget -O /usr/local/bin/aws-sudo
https://raw.githubusercontent.com/cleardataeng/aws-sudo/master/aws-sudo.sh &&
\  
chmod +x /usr/local/bin/aws-sudo  
  
RUN touch ~/.profile \  
&& chmod 750 ~/.profile \  
&& echo "if [ -f ~/.bashrc ]; then" >> ~/.profile \  
&& echo " . ~/.bashrc" >> ~/.profile \  
&& echo "fi" >> ~/.profile \  
&& touch ~/.bashrc \  
&& chmod 750 ~/.bashrc \  
&& echo "export GOROOT=/usr/local/go" >> ~/.bashrc \  
&& echo "export GOPATH=/f/projects/go" >> ~/.bashrc \  
&& echo "export PATH=/f/projects/go/bin:/usr/local/go/bin:$PATH" >> ~/.bashrc
\  
&& echo "cp -rf /root/ssh_temp /root/.ssh/" >> ~/.bashrc \  
&& echo "chmod -R 600 /root/.ssh" >> ~/.bashrc \  
&& echo "alias l='ls -CF'" >> ~/.bashrc \  
&& echo "alias la='ls -A'" >> ~/.bashrc \  
&& echo "alias ll='ls -alF'" >> ~/.bashrc \  
&& echo "alias ls='ls --color=auto'" >> ~/.bashrc \  
&& echo "source /etc/profile.d/bash_completion.sh" >> ~/.bashrc \  
&& echo "if [ -n '\$SSH_AUTH_SOCK' ] ; then" >> ~/.bashrc \  
&& echo " eval \$(ssh-agent -s)" >> ~/.bashrc \  
&& echo " ssh-add" >> ~/.bashrc \  
&& echo "fi" >> ~/.bashrc \  
&& echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc \  
&& echo "export PROJECT_HOME=/f/projects/go/src/gitlab.eng.cleardata.com" >>
~/.bashrc \  
&& echo "source /usr/bin/virtualenvwrapper.sh" >> ~/.bashrc \  
&& echo "" >> ~/.bashrc \  
&& sed -i 's/\/root:\/bin\/ash/\/root:\/bin\/bash/g' /etc/passwd \  
&& ln -s /usr/bin/pip3 /usr/local/bin/pip \  
&& ln -s /usr/bin/python3 /usr/local/bin/python  
  
RUN pip install awscli click rfc3987 downtoearth virtualenv virtualenvwrapper  
RUN pip install azure-cli  
RUN pip install awsrequests  
  
RUN wget
https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip  
RUN wget
https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip  
RUN unzip -o packer_*_linux_amd64.zip -d /usr/local/bin/  
RUN unzip -o terraform_*_linux_amd64.zip -d /usr/local/bin/  
RUN rm packer_*.zip  
RUN rm terraform_*.zip  
RUN chmod +x /usr/local/bin/packer  
RUN chmod +x /usr/local/bin/terraform  
  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash  
  
WORKDIR /root/  
  
CMD ["bash", "-il"]  

