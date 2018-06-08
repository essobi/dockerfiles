FROM ubuntu:14.04  
MAINTAINER Maksym Bodnarchuk <bodnarchuk@gmail.com>  
  
ENV REFRESHED_AT 2014-09-24  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties wget  
RUN add-apt-repository ppa:webupd8team/java -y  
  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get install -y oracle-java7-installer  
  
RUN wget -O /bin/lein
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein  
RUN chmod a+x /bin/lein  
RUN lein  
  
RUN lein new app draft  
  
VOLUME ["/draft"]  
  
WORKDIR /draft  
  
ENTRYPOINT ["lein"]  
  
CMD ["repl"]  

