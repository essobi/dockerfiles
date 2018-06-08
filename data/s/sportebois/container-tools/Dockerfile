# Ubuntu Sandbox - with all the command line we should need for any test  
#  
# Featuring  
# git svn  
# wget curl openssh  
# nodejs python go  
# jq  
# parallel  
# bc  
# xml2json  
# awscli  
# csvkit:  
# csvcut csvgrep csvjson csvpy csvsql csvstat  
# csvclean csvformat csvjoin csvlook csvsort csvstack  
# Data scennce tools  
# Rio Rio-mds Rio-pca Rio-scatter  
# cols dseq header scrape weka weka-cluster  
# arff2csv csv2arff dumbplot pbc servewd  
# body drake explain sample unpack  
FROM ubuntu:14.04  
MAINTAINER Sébastien Portebois <sportebois@tribalnova.com>  
  
  
# make sure the package repository is up to date  
RUN apt-get update  
RUN apt-get install -y \  
coreutils sudo bash wget curl grep sed mawk ssh openssh-client \  
git subversion tar tree nano \  
jq parallel bc gccgo-go  
  
# Install Python Setuptools  
# RUN apt-get install -y python-setuptools  
# Install pip  
# RUN easy_install pip  
RUN apt-get install python  
RUN apt-get install -y python-pip  
  
# NodeJS  
# RUN curl -sL https://deb .nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs npm  
# Make sure NodeJS is Node (and node nodejs) so that shebangs works!  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
RUN npm install -g xml2json-command  
  
RUN pip install csvkit  
# imagemagick  
ENV GOPATH /home/dev/go  
RUN env GOPATH=/home/dev/go  
RUN export GOPATH=/home/dev/go  
RUN go get github.com/jehiah/json2csv  
RUN apt-get install -y less  
RUN pip install awscli  
# RUN pip install bigmler skll  
RUN apt-get install -y python-lxml  
RUN pip install cssselect  
  
# Copy data tools  
WORKDIR ~  
ADD ./tools ~/tools  
ADD ./utils ~/utils  
RUN chmod +x /~/tools/*  
RUN chmod +x /~/utils/*  
ADD setup.sh /tmp/setup.sh  
RUN chmod +x /tmp/setup.sh  
  
ADD bash_prompt /home/.bash_prompt  
  
RUN \  
echo 'export PATH=$PATH:/~/tools/' >> ~/.bashrc ; \  
echo 'export PATH=$PATH:/~/utils/' >> ~/.bashrc ; \  
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc ; \  
echo "source /home/.bash_prompt" >> ~/.bashrc ;  
  
VOLUME ["/home"]  
  
CMD ["/bin/bash"]

