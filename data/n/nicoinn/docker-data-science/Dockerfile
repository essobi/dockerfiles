FROM ubuntu:18.04  
#Set the time zone  
ENV TZ=Europe/Stockholm  
  
  
#Commit the time zone configuration  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
COPY pkglist_* /  
  
RUN apt-get update && apt-get install -y --no-install-recommends `cat
pkglist_apt | awk '($1!~/^#/) && ($1!~/^$/) {print $1}' ` \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
  
#Install Python 2 packages  
RUN python2 -m pip install `cat /pkglist_python | awk '($1!~/^#/) &&
($1!~/^$/) {print $1}'`  
  
#Install Python 3 packages  
RUN python3 -m pip install `cat /pkglist_python | awk '($1!~/^#/) &&
($1!~/^$/) {print $1}'`  
  

