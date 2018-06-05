# Create a directory in /var/backups called "borg" in order to put the
repository (server side)  
# Will be the base to the server and the client version of the container  
FROM debian:latest  
  
# Which borg version to download  
# {freebsd64, linux32, linux64, macosx64}  
ENV ARCH linux64  
  
# Prepare environment, create user, etc...  
ENV LANG C.UTF-8  
RUN ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
RUN adduser --disabled-password --gecos "Borg Backup" \--quiet borg && \  
mkdir -p /var/run/sshd && \  
mkdir -p /var/backups/borg && \  
mkdir -p /home/borg/.ssh && \  
mkdir -p /home/borg/data  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -y \  
&& apt-get install -y \  
build-essential \  
fuse \  
libacl1-dev \  
libfuse-dev \  
liblz4-dev \  
liblzma-dev \  
libssl-dev \  
openssh-server \  
pkg-config \  
python3-virtualenv \  
python3-dev \  
python3-pip \  
wget \  
curl \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y --purge  
  
# Some more clean  
RUN rm -f /etc/ssh/ssh_host_*  
  
# Remove Password authentication and disable root login from ssh configuration  
RUN sed -i -e 's/^#PasswordAuthentication yes$/PasswordAuthentication no/g' \  
-e 's/^PermitRootLogin without-password$/PermitRootLogin no/g' \  
/etc/ssh/sshd_config  
  
# Install Borg using the latest release from GitHub  
WORKDIR /tmp  
RUN curl https://api.github.com/repos/borgbackup/borg/releases/latest | grep
"browser_download_url" | grep $ARCH | grep -v ".asc" | cut -d : -f 2,3 | tr -d
\" | wget -i -  
RUN mv borg* /usr/local/bin/borg && chown root:root /usr/local/bin/borg &&
chmod 755 /usr/local/bin/borg  
  
COPY entrypoint.sh /borg-server.sh  
RUN chmod +x /borg-server.sh  
  
ENTRYPOINT ["/borg-server.sh"]  
CMD ["start"]  

