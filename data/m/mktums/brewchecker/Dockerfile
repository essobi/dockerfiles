FROM ubuntu  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q \  
build-essential ruby python2.7 python2.7-dev python-pip git mercurial bzr \  
subversion curl libcurl4-gnutls-dev cvs fossil && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install
https://github.com/mktums/brewchecker/releases/download/v0.2.1/brewchecker-0.2.1.tar.gz  
ENTRYPOINT ["brewchecker"]  

