# meedan/awscli  
FROM meedan/base  
MAINTAINER sysops@meedan.com  
  
# aws cli  
RUN apt-get -qy install \  
python3 \  
python-pip \  
groff  
  
RUN pip install awscli s3cmd --upgrade --user  
  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/.local/bin  
  
# aws command completion  
RUN echo "complete -C '/root/.local/bin/aws_completer' aws" >> ~/.bashrc  
  
CMD ["/bin/bash"]

