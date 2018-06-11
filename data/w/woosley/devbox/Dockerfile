From centos:7  
run yum install -y epel-release  
run yum install -y git gcc vim-enhanced automake gcc-g++ make tmux  
# for pyenv  
run yum install -y sqlite-devel bzip2-devel readline-devel zlib-devel openssl-
devel  
# install pyenv  
run curl -L https://raw.githubusercontent.com/pyenv/pyenv-
installer/master/bin/pyenv-installer | bash  
run echo 'export PATH="/root/.pyenv/bin:$PATH"' >> /root/.bashrc && echo 'eval
"$(pyenv init -)"' >>/root/.bashrc && echo 'eval "$(pyenv virtualenv-init -)"'
>>/root/.bashrc  
  
# install python3.6  
run source /root/.bashrc && pyenv install 3.6.3  
run echo '3.6.3' > /root/.python-version  
ENV PYENV_VERSION 3.6.3  
# install a set of tools  
run source /root/.bashrc && pip3 install ansible httpie powerline-status
jupyter  
  
# replace yum.conf and reinstall glibc-common, this will bring all the locale
back  
run sed -i 's/^override/#override/g' /etc/yum.conf; yum -y reinstall glibc-
common  
ENV LC_ALL=zh_CN.UTF-8  

