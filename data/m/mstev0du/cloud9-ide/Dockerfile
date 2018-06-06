#
------------------------------------------------------------------------------  
# Based on work at https://github/mst3v3nsn/cloud9-ide.git  
#
------------------------------------------------------------------------------  
FROM ubuntu:16.04  
MAINTAINER mwsteven@odu.edu  
#
------------------------------------------------------------------------------  
# Change HOME for permission fix  
#
------------------------------------------------------------------------------  
ENV HOME=/c9files  
#
------------------------------------------------------------------------------  
# add entrypoint user for uid/gid mapping  
#
------------------------------------------------------------------------------  
RUN addgroup --gid 1000 c9user && \  
adduser --uid 1000 --ingroup c9user --home /c9files --shell /bin/sh
--disabled-password --gecos "" c9user  
#
------------------------------------------------------------------------------  
# Install base  
#
------------------------------------------------------------------------------  
RUN apt-get update  
RUN apt-get install -y build-essential g++ curl libssl-dev apache2-utils git
libxml2-dev nfs-common vim nano  
#
------------------------------------------------------------------------------  
# uid/gid parsing support  
#
------------------------------------------------------------------------------  
RUN USER=c9user && \  
GROUP=c9user && \  
curl -SsL
https://github.com/boxboat/fixuid/releases/download/v0.3/fixuid-0.3-linux-
amd64.tar.gz | tar -C /usr/local/bin -xzf - && \  
chown root:root /usr/local/bin/fixuid && \  
chmod 4755 /usr/local/bin/fixuid && \  
mkdir -p /etc/fixuid && \  
printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml  
#
------------------------------------------------------------------------------  
# Install Node.js  
#
------------------------------------------------------------------------------  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
#
------------------------------------------------------------------------------  
# Install Cloud9 SDK  
#
------------------------------------------------------------------------------  
RUN git clone https://github.com/c9/core.git /cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
#
------------------------------------------------------------------------------  
# update depreciated modules  
#
------------------------------------------------------------------------------  
RUN npm install pug-cli -g  
RUN npm install -g minimatch@3.0.2  
#
------------------------------------------------------------------------------  
# Tweak standlone.js conf  
#
------------------------------------------------------------------------------  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
#
------------------------------------------------------------------------------  
# Add volumes  
#
------------------------------------------------------------------------------  
RUN mkdir /workspace  
RUN mkdir /workspace/.c9  
#
------------------------------------------------------------------------------  
# add group support  
#
------------------------------------------------------------------------------  
# local groups needed in the image would be added here  
#
------------------------------------------------------------------------------  
# Clean up APT when done  
#
------------------------------------------------------------------------------  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#
------------------------------------------------------------------------------  
# allow binding for and application running for non-root  
#
------------------------------------------------------------------------------  
RUN setcap 'cap_net_bind_service=+ep' /usr/bin/node  
RUN chown -R c9user:c9user /cloud9  
RUN chown -R c9user:c9user /c9files  
RUN chown -R c9user:c9user /workspace  
RUN npm i --production  
#
------------------------------------------------------------------------------  
# Expose ports.  
#
------------------------------------------------------------------------------  
EXPOSE 80  
EXPOSE 3000  
#
------------------------------------------------------------------------------  
# Startup commands and entrypoint  
#
------------------------------------------------------------------------------  
ENTRYPOINT ["fixuid"]  
CMD ["/bin/sh", "-c", "/usr/bin/node /cloud9/server.js --listen 0.0.0.0 --port
80 -w /workspace"]  
#
------------------------------------------------------------------------------  
# switch user  
#
------------------------------------------------------------------------------  
USER c9user:c9user  

