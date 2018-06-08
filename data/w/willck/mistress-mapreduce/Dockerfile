FROM ubuntu  
  
MAINTAINER Will Childs-Klein <will.childsklein@gmail.com>  
  
# install dependencies and a few tools  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python \  
python-pip \  
curl \  
git  
  
# fine ALL the bins  
ENV PATH /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin  
  
# clone code repo and pull data  
RUN mkdir -p /mistress-mapreduce \  
&& git clone https://github.com/WillChilds-Klein/mistress-mapreduce.git
/mistress-mapreduce \  
&& mkdir /mistress-mapreduce/input \  
/mistress-mapreduce/output \  
/mistress-mapreduce/timer \  
&& curl -SL https://dl.dropboxusercontent.com/u/19937132/enron-email-
text.tar.gz \  
| tar -xzC /mistress-mapreduce/input  
  
# set workdir, install code and generate input_paths.txt  
WORKDIR /mistress-mapreduce  
RUN python ./setup.py install \  
&& scripts/generate_input_paths.sh  

