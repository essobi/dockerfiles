# The container runs a Git server on Ubuntu 14.04  
# with SSH support  
FROM nepalez/ubuntu-ssh  
MAINTAINER Andrew Kozin <andrew.kozin@gmail.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Setup git from official APT  
RUN apt-get install -y -qq software-properties-common && \  
add-apt-repository -y ppa:git-core/ppa && \  
apt-get update -qq && \  
apt-get install -y -qq git && \  
apt-get clean -qq  
  
# Create 'git' user  
RUN adduser git \  
\--shell $(which git-shell) \  
\--disabled-password \  
\--gecos "" && \  
chown git /home/git  
  
# Set a git repository to be default  
WORKDIR /home/git  
  
# Run SSH-server  
CMD ["service", "ssh", "start"]  

