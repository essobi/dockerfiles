FROM node:8-stretch  
MAINTAINER LWB  
  
ENV REPOSITORY=GIT  
ENV BRANCH=master  
ENV DB_HOST=HOST  
ENV DB_USER=ADMIN  
ENV DB_PASSWORD=ADMIN  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends \  
git && \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /project  
  
EXPOSE 10065  
EXPOSE 10065/udp  
  
CMD [ "npm", "start" ]  

