FROM node  
  
RUN apt-get update  
RUN apt-get -f install  
RUN apt-get -y install ant  
RUN apt-get -y install wget  
RUN apt-get install -y xz-utils  
RUN wget -qO- "https://developer.salesforce.com/media/salesforce-
cli/sfdx-v5.99.1-d7efd75-linux-amd64.tar.xz" | tar xJf -  
RUN ./sfdx/install  
RUN export PATH=./sfdx/$(pwd):$PATH  
RUN sfdx force --help

