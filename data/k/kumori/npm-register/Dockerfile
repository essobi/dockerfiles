FROM alpine:3.4  
MAINTAINER Jeff Dickey  
  
# Install NodeJS and node-gyp deps  
RUN apk --no-cache add \  
g++ \  
gcc \  
make \  
bash \  
gnupg \  
paxctl \  
python \  
nodejs \  
linux-headers  
  
ARG user=register  
ARG group=register  
ARG uid=1000  
ARG gid=1000  
# If you bind mount a volume from the host or a data container,  
# ensure you use the same uid  
# Create user and group  
RUN addgroup -S -g ${gid} ${group} \  
&& adduser -D -S \  
-s /bin/bash \  
-h /srv/npm-register \  
-G ${group} \  
-u ${uid} \  
${user}  
  
# addgroup  
# addgroup [-g GID] [user_name] group_name  
# Add a group or add a user to a group  
# Options:  
# -g GID Group id  
# -S Create a system group  
#  
# adduser  
# adduser [OPTIONS] user_name  
# Add a user  
# Options:  
# -h DIR Home directory  
# -g GECOS GECOS field  
# -s SHELL Login shell  
# -G GRP Add user to existing group  
# -S Create a system user  
# -D Do not assign a password  
# -H Do not create home directory  
# -u UID User id  
# Deploy application  
COPY . /srv/npm-register  
WORKDIR /srv/npm-register  
RUN npm install \  
&& chown -R ${user}:${group} .  
  
# Share storage volume  
ENV NPM_REGISTER_FS_DIRECTORY /data  
VOLUME /data  
  
# Start application  
EXPOSE 3000  
USER ${user}  
ENV NODE_ENV production  
CMD ["npm", "start"]  
  

