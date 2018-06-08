FROM tiredofit/nodejs:4-latest  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
  
### Set Environment Variables  
ENV RC_VERSION=0.59.1 \  
# needs a mongoinstance - defaults to container linking with alias 'db'  
MONGO_URL=mongodb://db:27017/meteor \  
HOME=/tmp \  
PORT=3000 \  
ROOT_URL=http://localhost:3000 \  
Accounts_AvatarStorePath=/app/uploads/avatars  
  
### Create Accounts  
RUN addgroup -g 1100 rocketchat && \  
adduser -Ss /bin/false -u 1100 -G rocketchat -h /app rocketchat && \  
mkdir -p /app/uploads && \  
chown rocketchat:rocketchat /app/uploads  
  
### Build Rocketchat  
RUN apk update && \  
mkdir -p /usr/src && \  
curl -ssL https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub && \  
curl -ssL https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk -o glibc-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk && \  
rm -rf glibc-2.25-r0.apk && \  
apk add --no-cache \  
curl \  
g++ \  
make \  
python && \  
cd /app && \  
curl -fssL "https://download.rocket.chat/build/rocket.chat-${RC_VERSION}.tgz"
| tar xvfz - -C /app/ && \  
cd /app/bundle/programs/server && \  
npm install  
  
### S6 Configuration  
ADD install/s6 /etc/s6  
  
### Networking Configuration  
EXPOSE 3000  
### Entrypoint Configuration  
WORKDIR /app/bundle  
ENTRYPOINT ["/init"]  
  

