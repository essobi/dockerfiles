FROM ubuntu:xenial  
  
ENV LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 TERM=xterm  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y build-essential locales software-properties-common nano
curl git htop man unzip wget && \  
sed -i -e "s/# $LANG.*/$LANG UTF-8/" /etc/locale.gen && \  
locale-gen --purge && \  
update-locale LANG=$LANG && \  
rm -rf /var/lib/apt/lists/*  
  
# Add files.  
ADD root/.bashrc_aliases /root/.bashrc_aliases  
#ADD root/.gitconfig /root/.gitconfig  
#ADD root/.scripts /root/.scripts  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]

