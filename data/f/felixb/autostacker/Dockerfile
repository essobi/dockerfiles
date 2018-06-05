FROM alpine  
  
ENTRYPOINT ["/usr/bin/autostacker24"]  
WORKDIR /workdir  
  
ENV \  
AUTOSTACKER_VERSION=2.8.1  
  
RUN apk add \--no-cache ruby ruby-json  
RUN gem install \  
\--version "=${AUTOSTACKER_VERSION}" \  
\--no-document \  
autostacker24  
  
USER nobody  

