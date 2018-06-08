  
#  
# Debian 8 (jessie) Nodejs dockerfile  
# Copyright (C) 2017 SOL-ICT  
# This file is part of the Nodejs.Stack.Docker.  
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
FROM solict/general-purpose-system-distro:debian8_minimal  
  
#  
# Arguments  
#  
ARG app_nodejs_version="4.7.3"  
ARG app_nodejs_arch="x64"  
ARG app_nodejs_env="production"  
ARG app_nodejs_user="nodejs"  
ARG app_nodejs_group="nodejs"  
ARG app_nodejs_home="/srv/nodejs"  
ARG app_nodejs_src="/srv/nodejs/src"  
ARG app_nodejs_data="/srv/nodejs/data"  
#  
# Environment  
#  
ENV NODE_VERSION="${app_nodejs_version}" \  
NODE_ARCH="${app_nodejs_arch}" \  
NODE_ENV="${app_nodejs_env}"  
#  
# Packages  
#  
RUN printf "Installing packages...\n" && \  
\  
printf "Add the GPG keys...\n" && \  
printf "\\- gpg keys listed at https://github.com/nodejs/node...\n" && \  
for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done && \  
\  
printf "Install the nodejs binaries...\n" && \  
wget "https://nodejs.org/dist/v${NODE_VERSION}/SHASUMS256.txt.asc" -O
"/tmp/nodejs-${NODE_VERSION}.asc" && \  
gpg --verify "/tmp/nodejs-${NODE_VERSION}.asc" && \  
wget
"https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.gz"
-O "/tmp/node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.gz" && \  
grep " node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.gz\$"
"/tmp/nodejs-${NODE_VERSION}.asc" | (cd "/tmp" && sha256sum -c -) && \  
tar -xzf "/tmp/node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.gz" -C
"/usr/local" \--strip-components=1 \  
\--exclude=CHANGELOG.md --exclude=LICENSE --exclude=README.md && \  
rm -f
"/tmp/{nodejs-${NODE_VERSION}.asc,node-v${NODE_VERSION}-linux-${NODE_ARCH}.tar.gz}"
&& \  
\  
printf "Cleanup the nodejs Package Manager...\n" && \  
$(which npm) cache clear && \  
\  
printf "Finished installing packages...\n";  
  
#  
# Nodejs modules  
#  
# Build and Install Nodejs modules  
RUN printf "Start installing modules...\n" && \  
\  
printf "Installing the PM2 module...\n" && \  
$(which npm) install -g pm2 && \  
\  
printf "\n# Checking modules...\n" && \  
$(which npm) list && \  
printf "Done checking modules...\n" && \  
\  
printf "Finished installing modules...\n";  
  
#  
# Configuration  
#  
# Add users and groups  
RUN printf "Adding users and groups...\n" && \  
\  
printf "Add nodejs user and group...\n" && \  
id -g "${app_nodejs_user}" || \  
groupadd \  
\--system "${app_nodejs_group}" && \  
id -u "${app_nodejs_user}" && \  
usermod \  
\--gid "${app_nodejs_group}" \  
\--home "${app_nodejs_home}" \  
\--shell "/sbin/nologin" \  
"${app_nodejs_user}" \  
|| \  
useradd \  
\--system --gid "${app_nodejs_group}" \  
\--no-create-home --home-dir "${app_nodejs_home}" \  
\--shell "/sbin/nologin" \  
"${app_nodejs_user}" && \  
\  
printf "Copying skeleton files...\n" && \  
rsync -rah "/etc/skel/." "${app_nodejs_home}" && \  
\  
printf "Setting ownership and permissions...\n" && \  
mkdir -p "${app_nodejs_src}" "${app_nodejs_data}" && \  
chown -R "${app_nodejs_user}":"${app_nodejs_group}" "${app_nodejs_home}" && \  
\  
printf "Finished adding users and groups...\n";  
  
# Nodejs  
RUN printf "Updading Nodejs configuration...\n" && \  
\  
printf "\n# Testing configuration...\n" && \  
echo "Testing $(which node):" && $(which node) --version && \  
echo "Testing $(which npm):" && $(which npm) --version && \  
echo "Testing $(which pm2):" && $(which pm2) --version && \  
printf "Done testing configuration...\n" && \  
\  
printf "Finished updading Nodejs configuration...\n";  
  
#  
# Runtime  
#  
VOLUME "${app_nodejs_data}"  
#USER "${app_nodejs_user}"  
WORKDIR "${app_nodejs_src}"  
CMD ["$(which pm2-docker)", "main.js", "-i", "max"]  
HEALTHCHECK \--interval=5m --timeout=3s --retries=3 CMD "$(which pm2) ping
main || exit 1"  
  

