FROM node:0.10  
MAINTAINER Stephan Maximilian Huber "stephan@factorial.io"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y -q
chrpath libfreetype6 libfreetype6-dev libssl-dev libfontconfig1 python python-
dev python-distribute python-pip build-essential imagemagick  
  
RUN curl -O -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN mv phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin/  
RUN rm -f phantomjs-1.9.8-linux-x86_64.tar.bz2 && rm -rf
phantomjs-1.9.8-linux-x86_64/bin/phantomjs  
  
RUN pip install dpxdt  
  
RUN git clone https://github.com/factorial-io/beautify-dpxdt.git  
RUN cd beautify-dpxdt && pip install -r requirements.txt  
  
ADD dpxdt_proxy.sh /usr/local/bin/dpxdt_proxy.sh  
  
VOLUME ["/tests", "/tmp"]  
  
ENTRYPOINT ["/usr/local/bin/dpxdt_proxy.sh"]  

