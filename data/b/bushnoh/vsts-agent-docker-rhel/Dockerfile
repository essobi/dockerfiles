FROM bushnoh/vsts-agent-docker-rhel:centos-7.2-docker-1.13.1  
# Install packages  
RUN yum -y install \  
python-pip git gcc python-devel \  
dh-autoreconf curl-devel expat-devel gettext-devel openssl-devel perl-devel
zlib-devel wget\  
&& yum clean all  
  
RUN wget https://www.kernel.org/pub/software/scm/git/git-2.12.2.tar.gz \  
-O /tmp/git-2.12.2.tar.gz \  
&& cd /tmp/ \  
&& tar xzf git-2.12.2.tar.gz \  
&& cd /tmp/git-2.12.2 \  
&& make prefix=/usr/local/git all \  
&& make prefix=/usr/local/git install \  
&& yum -y remove git \  
&& ln -s /usr/local/git/bin/git /usr/bin/git \  
&& rm -rf /tmp/git-2.12.2.tar.gz /tmp/git-2.12.2  
  
RUN yum -y reinstall glibc-common \  
&& localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& localedef -i en_GB -f UTF-8 en_GB.UTF-8 \  
&& yum clean all  
  
RUN pip install --upgrade pip docker-py \  
&& pip install git+git://github.com/ansible/ansible.git@v2.3.0.0-1  

