#Retrived from : docker history --no-trunc nbrun/svn-client  
FROM debian:wheezy  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget -q -O - http://opensource.wandisco.com/wandisco-debian.gpg | apt-key
add -  
RUN echo "deb http://opensource.wandisco.com/debian/ wheezy svn17" >
/etc/apt/sources.list.d/wandisco-subversion.list  
  
RUN apt-get update  
RUN apt-get install -y subversion subversion-tools  
  
RUN echo "store-plaintext-passwords = no" >> /etc/subversion/servers  

