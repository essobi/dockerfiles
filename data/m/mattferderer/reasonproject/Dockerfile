FROM ubuntu  
## Update apt-get - only show errors  
RUN apt-get -qq update  
## Add curl, git & m4.  
## m4 may not be needed in the future - follow:  
## https://github.com/reasonml/ReasonProject/issues/7  
## https://github.com/facebook/reason/issues/867  
RUN apt-get install -y curl git m4 ocaml apt-utils  
## Add npm  
## RUN apt-get install -y npm  
## Add repository for node v7  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
## Add nodejs & build-essential  
RUN apt-get install -y nodejs build-essential  
## Make node call nodejs since most packages expect node but Ubuntu refers to
it as nodejs  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
## Add VOLUME projects to host & set as working directory  
VOLUME ["/ReasonProject"]  
WORKDIR "/ReasonProject"  
CMD bash

