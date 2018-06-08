# Mattermost  
FROM debian:stretch  
LABEL maintainer = "s7b4 <baron.stephane@gmail.com>"  
  
ENV APP_VERSION=4.9.1 \  
APP_USER=mattermost  
  
# set user/group IDs  
RUN groupadd -r "$APP_USER" \--gid=999 && useradd -m -r -g "$APP_USER"
\--uid=999 "$APP_USER"  
  
# Base  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes \  
ca-certificates \  
curl \  
jq \  
netcat \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Mattermost  
RUN mkdir -p /opt/mattermost \  
&& curl -s "https://releases.mattermost.com/$APP_VERSION/mattermost-
team-$APP_VERSION-linux-$(dpkg --print-architecture | awk -F- '{ print $NF
}').tar.gz" | \  
tar xzf - --directory /opt/mattermost --strip-components 1  
  
COPY scripts/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8065  
VOLUME /home/$APP_USER

