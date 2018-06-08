from centos:latest  
maintainer octaltree<octaltree@gmail.com>  
  
ARG dns="dummy"  
workdir /tmp  
run if [ $dns != "dummy" ]; then echo $dns dns >> /etc/hosts; fi &&\  
cat /etc/hosts &&\  
yum update -y &&\  
yum install -y\  
zlib-devel\  
postgresql.x86_64\  
postgresql-devel.x86_64 &&\  
curl -sSL https://get.haskellstack.org/ | sh &&\  
stack upgrade &&\  
stack setup --install-ghc &&\  
stack install yesod-bin &&\  
stack path| grep local-bin-path| awk '{print $2}'| xargs -L1 -i echo 'export
PATH="$PATH:{}"' >> /root/.bashrc &&\  
yum clean all  
workdir /root  
cmd bash  

