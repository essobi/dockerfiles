FROM phusion/baseimage:0.9.19  
MAINTAINER Satoshi KAMEI "skame@nttv6.jp"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update && apt upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt install -y --no-install-recommends software-properties-common sudo \  
git-core nkf \  
curl wget  
ENV DEBIAN_FRONTEND noninteractive  
  
# locale  
RUN apt install -y --no-install-recommends language-pack-ja && export
LANG=ja_JP.UTF-8 && update-locale LANG=ja_JP.UTF-8  
  
# for sshd  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
# for sudo  
RUN echo 'skame ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
# for local account (used when ldap failed)  
RUN echo "skame:x:1039:1000::/home/skame:/usr/bin/zsh" >>/etc/passwd && echo
"skame:*:16737:0:99999:7:::" >>/etc/shadow && mkdir /home/skame && mkdir
/home/skame/.ssh && chown 1039 /home/skame/.ssh  
RUN echo ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQCZF2/4elfFD6ZAOQH62hvWj1Cyuhg/4ghz1mhl66ynNBDhkYGp94OjBS1PuroEkaLkP44XiYXCMFKbPODbWfLPElpb0kK/9kzEvUAo8AE/Ok9Ffvg/MN3bbgLHFvwdrTvtKmn3JdcEe52WXeRoF2bpqmPo8VejcKpQVUt0+keYCQXzcy8ZrlOy7mk1sPh2G5PkqK2TkwKTpvS0STRID3vZi2jLUAVD6nm/deNpbyng6oS8R57kT9so3pj0QmZkWb4qOneeSXa0CvCXcrPsn0ATQvDXsxXXzoMucs8a76HzmifleJvyqbkDq/Bu2Ua8DeBsn97aijS7QZymB1qVP4id
PIV AUTH pubkey > /home/skame/.ssh/authorized_keys  
RUN chown -R 1039 /home/skame/.ssh && chmod -R 0600 /home/skame/.ssh && chmod
o+x /home/skame/.ssh  
  
# docker and utilities  
RUN apt install -y --no-install-recommends docker.io  
  
RUN curl -s -L https://github.com/docker/compose/releases/latest | \  
egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-
Linux-x86_64' | \  
wget --base=http://github.com/ -i - -O /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose && \  
/usr/local/bin/docker-compose --version  
  
# some programming languages  
RUN apt install -y --no-install-recommends openjdk-8-jdk  
RUN apt install -y --no-install-recommends python3-pip  
RUN pip3 install awscli  
  
# some useful softwares  
RUN apt install -y --no-install-recommends zsh tmux emacs w3m owncloud-client-
cmd rsync man telnet redis-tools dnsutils jq postgresql-client mysql-client bc
ash  
  
# add db  
RUN apt install -y --no-install-recommends mysql-client  
# misc  
RUN apt install -y --no-install-recommends inetutils-ping traceroute net-tools  
  
# BEEEEEEEELINE  
RUN wget -O - http://package.mapr.com/releases/pub/maprgpg.key | sudo apt-key
add -  
RUN echo "deb http://package.mapr.com/releases/v5.2.0/ubuntu/ mapr optional"
>> /etc/apt/sources.list  
RUN echo "deb http://package.mapr.com/releases/ecosystem-5.x/ubuntu binary/"
>> /etc/apt/sources.list  
RUN apt-get update && apt install -y --no-install-recommends --allow-
unauthenticated mapr-hive  
RUN ln -s /opt/mapr/hive/hive-1.2/bin/beeline /usr/bin/beeline  
  
# Presto CLI  
RUN curl -s -L https://prestodb.io/docs/current/installation/cli.html | \  
egrep -o 'https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/[0-9.]+/presto-cli-[0-9.]+-executable.jar' | \  
wget -i - -O /usr/local/bin/presto && \  
chmod +x /usr/local/bin/presto && \  
/usr/local/bin/presto --version  
  
# Clean up APT when done.  
RUN apt clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
EXPOSE 22  

