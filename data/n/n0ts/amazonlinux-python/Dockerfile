FROM n0ts/amazonlinux  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
RUN set -x \  
&& yum install -y python2-pip python2-devel python2-virtualenv \  
&& pip-2 install --upgrade pip \  
&& python --version \  
&& pip --version  
  
CMD ["/bin/bash"]  

