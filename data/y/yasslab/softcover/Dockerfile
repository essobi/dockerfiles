FROM ruby:2.3  
MAINTAINER yasslab  
  
VOLUME /book  
WORKDIR /book  
  
RUN apt-get update  
  
RUN apt-get install -y texlive-lang-japanese texlive-fonts-recommended  
RUN apt-get install -y texlive-xetex inkscape zip default-jre fontconfig
calibre-bin  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN curl -sL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -jxf- -C /opt  
RUN mkdir -p /opt/kindlegen && curl -sL
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz | tar
-zxf- -C /opt/kindlegen  
  
ENV PATH $PATH:/opt/phantomjs-2.1.1-linux-x86_64/bin:/opt/kindlegen  
  
RUN gem install bundler epubcheck-ruby  

