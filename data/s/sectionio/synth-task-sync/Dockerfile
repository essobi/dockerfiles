FROM node:6.11-onbuild  
RUN sed 's@/archive.ubuntu.com/@/archive.ubuntu.com.section.io/@' -i
/etc/apt/sources.list  
RUN apt-get update && apt-get install -u jq  
RUN chmod +x /usr/src/app/kubectl  
RUN chmod +x /usr/src/app/create-tenant.sh  

