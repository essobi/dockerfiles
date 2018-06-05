FROM bytesized/debian-base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive &&
\  
apt-get update && \  
apt-get install -y -qq \  
curl \  
git  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 &&
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list && apt-get update && apt-get
install -y mongodb-org  
  
ENV MONGO_URL=mongodb://127.0.0.1:27017/plexrequests  
  
VOLUME /config  
  
COPY /static /  
  
EXPOSE 3000  

