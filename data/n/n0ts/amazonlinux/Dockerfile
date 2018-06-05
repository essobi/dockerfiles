FROM amazonlinux:2  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
ENV user ec2-user  
ENV group ec2-user  
ENV work /work  
  
RUN set -x \  
&& yum clean all \  
&& yum install -y wget \  
&& wget -r --no-parent -A 'epel-release-*.rpm'
http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/ \  
&& rpm -Uvh dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-
release-*.rpm \  
&& rm -fr dl.fedoraproject.org/ \  
&& yum upgrade -y \  
&& yum groupinstall -y "Development Tools" \  
&& yum install -y aws-cli \  
bash-completion \  
curl emacs git initscripts \  
jq \  
less the_silver_searcher \  
sudo tree unzip vim zsh \  
  
# add local user  
&& groupadd ${user} \  
&& useradd ${user} -g ${group} -m -s /bin/bash \  
&& echo "%${group} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/00-${group} \  
&& chmod 400 /etc/sudoers.d/00-${group} \  
  
# create work directory  
&& mkdir ${work} \  
&& chown -R ${user}:${group} ${work}  
  
CMD ["/bin/bash"]  

