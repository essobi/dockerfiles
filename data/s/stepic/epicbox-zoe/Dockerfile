FROM stepic/epicbox-base:latest  
MAINTAINER Pavel Sviderski <ps@stepic.org>  
  
RUN yum install -y epel-release && yum install -y gcc python-devel python-pip
&& yum clean all  
  
RUN pip install https://github.com/StepicOrg/stepic-pytest/tarball/develop  

