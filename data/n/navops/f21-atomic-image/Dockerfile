FROM fedora:21  
RUN cd /tmp && curl -O -L http://s3.amazonaws.com/ec2-downloads/ec2-ami-
tools.noarch.rpm \  
&& yum install -y \  
rpm-ostree-toolbox-2014.110-4.fc21 \  
git-2.1.0-5.fc21.x86_64 \  
ruby-2.1.7-31.fc21 \  
python-pip-1.5.6-3.fc21 \  
/tmp/ec2-ami-tools.noarch.rpm \  
&& rm /tmp/ec2-ami-tools.noarch.rpm \  
&& pip install awscli \  
&& yum clean all && rm -rf /var/cache/yum  

