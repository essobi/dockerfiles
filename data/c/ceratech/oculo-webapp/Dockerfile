FROM circleci/ruby:2.3.7-stretch-node-browsers  
MAINTAINER jdubs <jgw@oculo.com.au>  
  
RUN sudo apt-get update -qq  
RUN sudo apt-get install -y build-essential postgresql-client python-pip
python-dev libssl-dev  
RUN sudo pip install --upgrade pip  
RUN sudo pip install awsebcli  
# have had issues installing ghostscript, now that they are resolved(?) we  
# should be able to add these to the previous apt-get install  
RUN sudo apt-get install -y ghostscript imagemagick  

