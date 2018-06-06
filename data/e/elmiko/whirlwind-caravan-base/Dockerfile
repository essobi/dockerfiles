FROM elmiko/openshift-spark  
  
ADD requirements.txt /opt/whirlwind/requirements.txt  
  
RUN yum install -y epel-release gcc python-devel \  
&& yum install -y python-pip \  
&& pip install -r /opt/whirlwind/requirements.txt  

