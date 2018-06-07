#  
# Build stage  
#  
FROM node:6-alpine  
  
# Download parsoid sources  
ENV PARSOID_VERSION=0.5.3  
ADD https://github.com/wikimedia/parsoid/archive/v${PARSOID_VERSION}.tar.gz
/tmp  
RUN tar -xf /tmp/v${PARSOID_VERSION}.tar.gz -C /tmp/ &&\  
mv /tmp/parsoid-${PARSOID_VERSION} /root/parsoid  
WORKDIR /root/parsoid  
  
# Install dependencies  
RUN apk add --no-cache git make gcc g++ python  
RUN npm install --production  
  
#  
# Execution stage  
#  
FROM node:6-alpine  
  
# Enable health check  
RUN apk add --no-cache curl  
HEALTHCHECK \--interval=30s --timeout=3s --start-period=5s \  
CMD curl -f http://localhost:8000/_version || exit 1  
  
# Import prebuilt parsoid and a config file  
COPY \--from=0 /root/parsoid /srv/parsoid  
COPY localsettings.js /srv/parsoid/localsettings.js  
  
# Create a new unix user with limited access  
RUN adduser -D parsoid_user &&\  
chown -R parsoid_user:parsoid_user /srv/parsoid  
  
# Define entrypoint  
USER parsoid_user  
ENV NODE_ENV=production  
WORKDIR /srv/parsoid  
EXPOSE 8000  
ENTRYPOINT ["node", "bin/server.js"]  

