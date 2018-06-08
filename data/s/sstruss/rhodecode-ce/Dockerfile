FROM ubuntu:18.04  
#install all the necessary packages  
RUN apt update && apt install -y \  
curl vim bzip2 sudo libapr1-dev libaprutil1-dev libsvn-dev \  
postgresql postgresql-contrib libpq-dev libcurl4-openssl-dev mercurial  
  
#add nix build user and group  
RUN groupadd nixbld && useradd -g nixbld nixbld && usermod -G nixbld nixbld  
  
#download and install nix  
RUN curl https://nixos.org/nix/install | USER=root sh  
  
#update nix's package database  
RUN USER=root . /root/.nix-profile/etc/profile.d/nix.sh && \  
nix-channel --update && \  
nix-channel --add https://nixos.org/channels/nixos-16.03 nixpkgs && \  
nix-channel --update  
  
#preload nix-prefetch-*  
RUN USER=root . /root/.nix-profile/etc/profile.d/nix.sh && \  
nix-env -i nix-prefetch-hg && \  
nix-env -i nix-prefetch-git  
  
#download rhodecode enterprise and vcsserver  
RUN mkdir rhodecode-develop && \  
cd rhodecode-develop && \  
hg clone https://code.rhodecode.com/rhodecode-enterprise-ce -u v4.12.1 && \  
hg clone https://code.rhodecode.com/rhodecode-vcsserver -u v4.12.1  
  
#install rhodecode vcsserver  
RUN USER=root . /root/.nix-profile/etc/profile.d/nix.sh && \  
cd rhodecode-develop/rhodecode-vcsserver && \  
nix-shell  
  
#install rhodecode enterprise  
RUN USER=root . /root/.nix-profile/etc/profile.d/nix.sh && \  
cd rhodecode-develop/rhodecode-enterprise-ce && \  
nix-shell  
  
#make sure nix has its configuration  
RUN mkdir -p ~/.nixpkgs && touch ~/.nixpkgs/config.nix  
  
#enable connections from all hosts for rhodecode enterprise (not vcsserver)  
RUN sed -i -e 's/host = .*/host = 0.0.0.0/' /rhodecode-develop/rhodecode-
enterprise-ce/configs/production.ini  
  
#create repositories directory  
RUN mkdir /root/my_dev_repos  
  
#copy nix's configuration  
COPY config.nix /root/.nixpkgs/config.nix  
  
#setup rhodecode enterprise to use postgres, use only one worker because of a
race condition currently occuring, create the database and let grunt do its
tasks  
RUN sed -i -e 's/postgres:qweqwe/postgres:postgres/' /rhodecode-
develop/rhodecode-enterprise-ce/configs/production.ini  
RUN sed -i -e 's/workers = 2/workers = 1/' /rhodecode-develop/rhodecode-
enterprise-ce/configs/production.ini  
RUN rm /etc/timezone  
  
RUN service postgresql start && \  
sudo -u postgres -H psql -c "ALTER USER postgres PASSWORD 'postgres';" && \  
sudo -u postgres -H psql -c "CREATE DATABASE rhodecode" && \  
USER=root . /root/.nix-profile/etc/profile.d/nix.sh && \  
cd rhodecode-develop/rhodecode-enterprise-ce && \  
nix-shell --run "rc-setup-app configs/production.ini --user=admin
--password=secret --email=admin@example.com --repos=/root/my_dev_repos
--force-yes && grunt"  
  
#generate the necessary locale to start the vcsserver/rhodecode enterprise  
RUN USER=root . /root/.nix-profile/etc/profile.d/nix.sh && nix-env -i glibc-
locales && export LOCALE_ARCHIVE=`nix-env --installed --no-name --out-path
--query glibc-locales`/lib/locale/locale-archive  
  
COPY start.sh /start.sh  
RUN chmod +x start.sh  
VOLUME /rhodecode-develop/rhodecode-enterprise-ce/configs /var/lib/postgresql
/root/my_dev_repos  
EXPOSE 5000  
CMD /start.sh  

