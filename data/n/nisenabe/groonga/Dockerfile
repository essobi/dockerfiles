FROM debian:wheezy  
MAINTAINER nise_nabe <nise.nabe@gmail.com>  
  
RUN apt-get -qq update && apt-get upgrade -y && apt-get clean  
  
RUN echo "deb http://packages.groonga.org/debian/ wheezy main\ndeb-src
http://packages.groonga.org/debian/ wheezy main" >>
/etc/apt/sources.list.d/groonga.list \  
&& apt-get -qq update \  
&& apt-get -y --allow-unauthenticated install groonga-keyring \  
&& apt-get -qq update \  
&& apt-get -y install groonga groonga-tokenizer-mecab \  
&& apt-get clean  
  
EXPOSE 10041  
CMD groonga -d --protocol http -n /tmp/groonga.db && tail -f /dev/null  

