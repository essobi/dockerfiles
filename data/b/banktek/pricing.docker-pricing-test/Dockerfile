FROM centos:6  
MAINTAINER Craig craig@bankteksystems.com.au  
#The following lines allow newer versions to be installed on centos6  
RUN yum -y update;yum -y install https://centos6.iuscommunity.org/ius-
release.rpm \  
&& yum -y install python-pip python36u python36u-devel python36u-pip python27
python27-devel \  
python27-pip wget git postgresql postgresql-server postgresql-devel python-
devel gcc nodejs \  
npm openldap-devel  
RUN npm install -g bower \  
&& pip install -U tox pylint wheel make-deb boto3==1.3.0 \  
&& useradd banktek;mkdir /apps;chown -R banktek /apps  
ADD requirements.txt /apps  
ADD pip.conf /home/banktek/.pip/pip.conf  
ADD pip.conf /root/.pip/pip.conf  
RUN mkdir /apps/.pip-wheelhouse \  
&& pip2.7 install wheel numpy cython; pip2.7 wheel -r /apps/requirements.txt \  
&& pip3.6 install wheel numpy cython; pip3.6 wheel -r /apps/requirements.txt  
USER banktek  
WORKDIR /apps  
CMD echo "Welcome to pricing/docker-pricing-test image..."  

