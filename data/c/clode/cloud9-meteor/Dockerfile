FROM program3r/cloud9-docker  
RUN apt-get update  
#Install Tools  
RUN apt-get install -y wget curl bzip2  
#Install PhantomJS  
RUN apt-get -y install libfreetype6 libfreetype6-dev fontconfig  
WORKDIR /usr/local/share/  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
> /dev/null  
RUN tar xjf phantomjs-1.9.8-linux-x86_64.tar.bz2 > /dev/null  
RUN ln -s -f /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
RUN ln -s -f /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN ln -s -f /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
  
RUN curl https://install.meteor.com/ | sh  
  
ENV ROOT_URL http://localhost  
ENV PORT 3000  

