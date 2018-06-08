FROM ubuntu:15.10  
MAINTAINER zyuyou yuyouchow@gmail.com  
  
# gettext for envsubst  
RUN apt-get update && apt-get install -yq samba gettext  
ADD share.tmpl /share.tmpl  
ADD setup.sh /setup.sh  
  
ENTRYPOINT ["/setup.sh"]  

