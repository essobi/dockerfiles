  
#  
# Debian 8 (jessie) Main dockerfile  
# Copyright (C) 2017 SOL-ICT  
# This file is part of the Rocket.Chat.Docker.  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
FROM solict/nodejs.stack.docker:debian8_nodejs  
  
#  
# Arguments  
#  
ARG app_main_version="latest"  
ARG app_main_user="rocketchat"  
ARG app_main_group="rocketchat"  
ARG app_main_home="/srv/rocketchat"  
ARG app_main_src="${app_main_home}/src"  
ARG app_main_data="${app_main_home}/data"  
ARG app_main_proto="http"  
ARG app_main_host="rocketchat-main"  
ARG app_main_port="3000"  
ARG app_mongodb_proto="mongodb"  
ARG app_mongodb_host="rocketchat-mongodb"  
ARG app_mongodb_port="27017"  
ARG app_mongodb_database="rocketchat"  
#  
# Environment  
#  
ENV RC_VERSION="${app_main_version}" \  
PORT="${app_main_port}" \  
ROOT_URL="${app_main_proto}://${app_main_host}:${app_main_port}" \  
MONGO_URL="${app_mongodb_proto}://${app_mongodb_host}:${app_mongodb_port}/${app_mongodb_database}"
\  
Accounts_AvatarStorePath="${app_main_data}/uploads"  
#  
# Packages  
#  
RUN printf "Installing packages...\n" && \  
\  
printf "Install the required packages...\n" && \  
apt-get update && apt-get install -qy \  
imagemagick && \  
printf "Cleanup the Package Manager...\n" && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
\  
printf "Finished installing packages...\n";  
  
#  
# Configuration  
#  
# Add users and groups  
RUN printf "Adding users and groups...\n" && \  
\  
printf "Add rocketchat user and group...\n" && \  
id -g "${app_main_user}" || \  
groupadd \  
\--system "${app_main_group}" && \  
id -u "${app_main_user}" && \  
usermod \  
\--gid "${app_main_group}" \  
\--home "${app_main_home}" \  
\--shell "/sbin/nologin" \  
"${app_main_user}" \  
|| \  
useradd \  
\--system --gid "${app_main_group}" \  
\--no-create-home --home-dir "${app_main_home}" \  
\--shell "/sbin/nologin" \  
"${app_main_user}" && \  
\  
printf "Copying skeleton files...\n" && \  
rsync -rah "/etc/skel/." "${app_main_home}" && \  
\  
printf "Setting ownership and permissions...\n" && \  
mkdir -p "${app_main_data}" && \  
chown -R "${app_main_user}":"${app_main_group}" "${app_main_home}" && \  
\  
printf "Finished adding users and groups...\n";  
  
#  
# Application  
#  
RUN printf "Installing application...\n" && \  
\  
printf "Add the GPG keys...\n" && \  
printf "\\- gpg key 4FD08014: public key Rocket.Chat Buildmaster
<buildmaster@rocket.chat>...\n" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
0E163286C20D07B9787EBE9FD7F9D0414FD08104 && \  
\  
printf "Install the binaries...\n" && \  
mkdir -p "${app_main_src}" && \  
wget "https://rocket.chat/releases/${RC_VERSION}/download" -O
"/tmp/rocket.chat-${RC_VERSION}.tar.gz" && \  
wget "https://rocket.chat/releases/${RC_VERSION}/asc" -O
"/tmp/rocket.chat-${RC_VERSION}.tar.gz.asc" && \  
gpg --verify "/tmp/rocket.chat-${RC_VERSION}.tar.gz.asc" && \  
tar -xzf "/tmp/rocket.chat-${RC_VERSION}.tar.gz" -C "${app_main_src}" && \  
rm -f
"/tmp/{rocket.chat-${RC_VERSION}.tar.gz.asc,rocket.chat-${RC_VERSION}.tar.gz}"
&& \  
\  
printf "Run the module installation...\n" && \  
(cd "${app_main_src}/bundle/programs/server" && $(which npm) install) && \  
\  
printf "Cleanup the nodejs Package Manager...\n" && \  
$(which npm) cache clear && \  
\  
printf "Finished installing application...\n";  
  
#  
# Runtime  
#  
EXPOSE $app_main_port  
VOLUME "${app_main_data}"  
USER "${app_main_user}"  
WORKDIR "${app_main_src}/bundle"  
CMD ["$(which pm2-docker)", "main.js", "-i", "max"]  
HEALTHCHECK \--interval=5m --timeout=3s --retries=3 CMD "$(which pm2) ping
main || exit 1"  
  

