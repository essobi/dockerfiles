FROM debian:jessie-slim  
RUN apt-get -y update  
RUN apt-get -y install rsync wget make python3  
RUN mkdir context && cd context && wget -O first-setup.sh
http://minimals.contextgarden.net/setup/first-setup.sh && chmod 755 first-
setup.sh && sh ./first-setup.sh \--modules=all \--engine=luatex  
ENV PATH="/context/tex/texmf-linux-64/bin:${PATH}"  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

