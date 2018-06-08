FROM ubuntu:17.04  
  
RUN apt-get update -y && apt-get upgrade -y \  
&& apt-get install -y apt-utils sysstat stress-ng tmux language-pack-en \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/bin/tmux", "-u", "-CC"]

