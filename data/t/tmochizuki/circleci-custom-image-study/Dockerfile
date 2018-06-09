FROM ubuntu:latest  
  
ENV user ubuntu  
ENV group ubuntu  
ENV work /work  
  
RUN set -x \  
&& apt update \  
&& apt upgrade -y \  
&& apt install -y apt-transport-https \  
build-essential bash-completion \  
ca-certificates curl emacs git \  
less silversearcher-ag \  
software-properties-common \  
sudo tree unzip vim wget \  
language-pack-en language-pack-ja \  
jq netcat telnet \  
mysql-client postgresql-client redis-tools \  
  
&& locale-gen \  
  
# add local user  
&& groupadd ${user} \  
&& useradd ${user} -g ${group} -m -s /bin/bash \  
&& echo "%${group} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/00-${group} \  
&& chmod 400 /etc/sudoers.d/00-${group} \  
  
# create work directory  
&& mkdir ${work} \  
&& chown -R ${user}:${group} ${work}  
  
CMD ["/bin/bash"]  

