FROM ubuntu:16.04  
MAINTAINER Jian Li <gunine@sk.com>  
  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends telnet build-essential gawk
wget texinfo supervisor iptables  
  
# Patch Quagga to support FPM  
ADD change.diff /tmp/change.diff  
RUN wget
http://download.savannah.gnu.org/releases/quagga/quagga-0.99.23.tar.gz  
RUN tar zxvf quagga-0.99.23.tar.gz  
WORKDIR /quagga-0.99.23  
RUN patch -p1 < /tmp/change.diff  
RUN ./configure --enable-fpm --prefix=/usr  
RUN make  
RUN make install  
  
# 179/tcp - bgp port  
# 2601/tcp - zebra management port  
# 2604/tcp - ospfd management port  
# 2605/tcp - bgpd management port  
EXPOSE 179 2601 2605  
# install prereqs  
RUN apt-get update && apt-get install --yes wget python vim bash-completion
gcc lsb-release  
  
# ubuntu's pip is too old to work with the version of requests we  
# require, so get pip with get-pip.py  
RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm -f get-pip.py  
  
# install bindep  
RUN pip install bindep  
  
# create rally user  
RUN apt-get install sudo && \  
useradd -u 65500 -m rally && \  
usermod -aG sudo rally && \  
echo "rally ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/00-rally-user && \  
ln -s /opt/rally/doc /home/rally/rally-docs  
  
# install rally. the COPY command below frequently invalidates  
# subsequent cache  
COPY . /tmp/rally  
WORKDIR /tmp/rally  
RUN ./install_rally.sh --system --verbose --yes \  
\--db-name /home/rally/.rally.sqlite && \  
pip install -r optional-requirements.txt && \  
mkdir /opt/rally/ && \  
# TODO(andreykurilin): build docs to rst before move, since we have several  
# extensions.  
mv certification/ samples/ doc/ /opt/rally/ && \  
chown -R rally /opt/rally /etc/rally && \  
rm -rf /tmp/* && \  
apt-get -y remove \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
python3 \  
&& \  
apt-get -y autoremove && \  
apt-get clean  
  
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/motd' \  
>> /etc/bash.bashrc; echo '\  
╔═════════════════════════════════════════════════════════════════════════════╗\n\  
║ Welcome to Rally Docker container! ║\n\  
║ Rally certification tasks, samples and docs are located at /opt/rally/ ║\n\  
║ Rally at readthedocs - http://rally.readthedocs.org ║\n\  
║ How to contribute - http://rally.readthedocs.org/en/latest/contribute.html
║\n\  
║ If you have any questions, you can reach the Rally team by: ║\n\  
║ * e-mail - openstack-dev@lists.openstack.org with tag [Rally] in subject
║\n\  
║ * irc - "#openstack-rally" channel at freenode.net ║\n\  
╚═════════════════════════════════════════════════════════════════════════════╝\n'
> /etc/motd  
  
VOLUME ["/home/rally"]  
  
WORKDIR /home/rally/  
USER rally  
ENV HOME /home/rally/  
# CMD ["bash", "--login"]  
RUN rally-manage db recreate  
  
WORKDIR /  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ENTRYPOINT ["/usr/bin/supervisord"]  

