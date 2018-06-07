FROM rpawel/ubuntu:trusty  
  
RUN add-apt-repository -y ppa:duplicity-team/ppa \  
&& apt-get -q -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-pip duplicity
duply python-yaml \  
&& pip install boto  
  

