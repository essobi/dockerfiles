FROM opensuse:13.1  
RUN zypper --non-interactive --gpg-auto-import-keys ref  
RUN zypper in -y gcc \  
libopenssl-devel \  
make \  
ruby \  
ruby-devel  
RUN gem install bson_ext \  
etcd \  
mongo \  
puma \  
sinatra  
  
ADD code /code  
  
WORKDIR /code  

