FROM node:5.4  
MAINTAINER Andras Kosztyu, kosztyua@vipcomputer.hu  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -yq \  
git  
  
RUN git clone https://github.com/seejohnrun/haste-server.git /app  
WORKDIR /app  
RUN npm install  
  
ADD ./app.sh /app/  
RUN chmod 755 app.sh  
ADD ./haste-baseurl-patch-generator.pl /app/  
RUN perl haste-baseurl-patch-generator.pl bin  
RUN patch -p0 < baseurl.patch  
  
EXPOSE 7777  
CMD [ "./app.sh" ]  

