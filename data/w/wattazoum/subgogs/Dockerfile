FROM gogs/gogs:0.9.71  
MAINTAINER Oumar Aziz OUATTARA (wattazoum)  
  
RUN apk --update add wget openjdk8 subversion  
  
RUN wget -q --no-check-certificate
https://subgit.com/download/subgit-3.2.2.zip -O /tmp/subgit.zip  
  
RUN unzip /tmp/subgit.zip -d /usr/local/share/ && ln -s
/usr/local/share/subgit* /usr/local/share/subgit  
  
ENV PATH /usr/local/share/subgit/bin:$PATH  
  
RUN rm /tmp/subgit.zip  
  

