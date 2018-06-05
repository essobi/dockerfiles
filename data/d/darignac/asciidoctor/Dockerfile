FROM openjdk:jre  
  
LABEL maintainer="Alexander Herrmann <darignac@gmail.com>"  
  
#RUN apk update && apk upgrade  
#RUN apk add ruby ruby-dev ruby-bundler build-base zlib-dev  
#RUN apk add graphviz  
#RUN apk add icu icu-libs icu-dev  
RUN apt-get update && apt-get upgrade -y && apt-get install -y ruby graphviz
ruby-dev build-essential zlib1g-dev  
  
RUN gem install --no-ri --no-rdoc json  
RUN gem install --no-ri --no-rdoc asciidoctor --version 1.5.6.1  
RUN gem install --no-ri --no-rdoc asciidoctor-diagram --version 1.5.8  
RUN gem install --no-ri --no-rdoc asciidoctor-epub3 --version 1.5.0.alpha.8  
RUN gem install --no-ri --no-rdoc asciidoctor-pdf --version 1.5.0.alpha.16  
RUN gem install --no-ri --no-rdoc asciidoctor-revealjs --version 1.1.3  
  
#RUN rm -rf /var/cache/apk/*  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /documents  
WORKDIR /documents  
VOLUME /documents  

