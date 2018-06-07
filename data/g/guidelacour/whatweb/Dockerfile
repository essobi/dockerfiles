FROM ruby:2.2  
ENV WHATWEB_VERSION master  
  
RUN gem install rchardet mongo json  
RUN git clone \--branch $WHATWEB_VERSION
https://github.com/urbanadventurer/WhatWeb.git /src/whatweb  
  
WORKDIR /src/whatweb  
  
CMD /src/whatweb/whatweb  

