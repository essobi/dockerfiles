FROM cptactionhank/atlassian-jira-software:latest  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
# grsec compatibility  
# - switch to root user  
# - install paxctl  
# - disable MPROTECT on the java binary  
# - remove paxctl  
# - switch back to daemon user  
  
USER root:root  
  
COPY java-pax.sh /root/java-pax.sh  
RUN chmod +x /root/java-pax.sh  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
paxctl \  
&& /root/java-pax.sh \  
&& apt-get -y --purge purge paxctl \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
USER daemon:daemon  

