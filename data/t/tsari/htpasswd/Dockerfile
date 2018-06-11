# !/bin/bash  
# docker run -it \  
# \--env="USER" \  
# \--env="UID=$(id -u)" \  
# \--env="GID=$(id -g)" \  
# \--volume="$PWD:/workingDir" \  
# tsari/htpasswd "$@"  
#  
# or for sudo usage...  
#  
#!/bin/bash  
# user=$USER  
# uid=$(id -u)  
# gid=$(id -g)  
# sudo docker run -it --rm \  
# -e "USER=$user" \  
# -e "UID=$uid" \  
# -e "GID=$gid" \  
# \--volume="$PWD:/workingDir" \  
# tsari/htpasswd "$@"  
FROM debian:stable  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
RUN apt-get update -qq && \  
apt-get install --no-install-recommends -y \  
apache2-utils \  
sudo \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Set up the application directory  
VOLUME ["/workingDir"]  
WORKDIR /workingDir  
  
# Set up the command arguments  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "htpasswd"]

