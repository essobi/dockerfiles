FROM ubuntu:16.10  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
RUN apt-get update -q \  
&& apt-get dist-upgrade -qy \  
&& apt-get install -qyy wget curl build-essential cpp git \  
&& apt-get -qyy install python3.6 python3-pip python3-dev python3-setuptools
uwsgi-plugin-python3 \  
&& apt-get install python3.6-dev -qy \  
&& curl https://bootstrap.pypa.io/get-pip.py | python3.6 \  
&& pip install --upgrade pip \  
&& pip install numpy seqann pygfe \  
&& apt-get install clustalo -y \  
&& apt-get install ncbi-blast\+ -y  
  
RUN touch blank.fasta && seq2gfe -f blank.fasta -l HLA-A \  
&& seq2gfe -f blank.fasta -l KIR3DL2 -k  

