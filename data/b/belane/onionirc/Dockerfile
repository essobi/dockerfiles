FROM debian:latest  
MAINTAINER belane github.com/belane/docker-onionirc  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -y  
RUN apt-get install -y \  
weechat tor \  
\--no-install-recommends \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD /etc/init.d/tor start && bash -c "weechat --run-command '/proxy add tor
socks5 127.0.0.1 9050;/server add onionirc onionirchubx5363.onion/6697;/set
irc.server.onionirc.ssl on;/set irc.server.onionirc.ssl_fingerprint
e4384106a199610261082eb97fd972382a299a38;/set irc.server.onionirc.proxy
tor;/set irc.server.onionirc.nicks anon;/connect onionirc;/set
irc.look.smart_filter on;/filter add irc_smart * irc_smart_filter *;/set
irc.look.smart_filter_delay 1'"  

