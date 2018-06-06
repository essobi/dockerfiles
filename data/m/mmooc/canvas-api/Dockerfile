FROM ruby  
RUN apt-get -y update  
RUN apt-get -y install vim  
RUN apt-get -y install git  
WORKDIR /  
RUN git clone https://github.com/matematikk-mooc/canvas-api.git  
RUN gem install canvas-api  
ENV CURL_CA_BUNDLE=/canvas-api/mmooc.crt  
WORKDIR /canvas-api  
CMD /bin/bash

