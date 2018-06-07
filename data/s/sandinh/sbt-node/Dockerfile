FROM java:8  
ENV SBT_VERSION 0.13.12  
# http://serverfault.com/a/743015/179477  
# https://github.com/docker/docker/issues/1799#issuecomment-126083922  
RUN \  
echo $'Acquire::http::Pipeline-Depth 0;\n\  
Acquire::http::No-Cache true;\n\  
Acquire::BrokenProxy true;' \  
> /etc/apt/apt.conf.d/99fixbadproxy && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs sudo && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/*  
  
RUN \  
# Adds fs-extra to npm and replaces the fs.rename method with the fs.extra  
# move method that now automatic chooses what to do (rename/move).  
# See https://github.com/npm/npm/issues/9863  
cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js  
  
RUN npm install -g bower@1.7.9 gulp@3.9.1 grunt-cli@1.2.0 typings@1.3.2  
  
# https://docs.docker.com/engine/installation/binaries/  
RUN \  
curl https://get.docker.com/builds/Linux/x86_64/docker-1.12.0.tgz | tar xvz &&
\  
mv docker/docker /usr/bin/ && \  
rm -Rf docker/  
  
RUN \  
adduser --disabled-password --gecos "" sandinh && \  
echo 'sandinh ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN \  
curl -sL https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt >
/bin/sbt && \  
chmod 0755 /bin/sbt  
  
USER sandinh  
  
RUN \  
curl -sLk --create-dirs -o ~/.sbt/launchers/$SBT_VERSION/sbt-launch.jar \  
https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar  
  
# cant use alias because java ProcessBuilder - which sbt-native-packager use -
will not take that  
# when we run sbt docker:publishLocal  
# echo "alias docker='sudo docker'" > ~/.bash_aliases && \  
RUN \  
mkdir ~/bin && \  
echo '#!/usr/bin/env bash\nsudo /usr/bin/docker "$@"\n' > ~/bin/docker && \  
chmod +x ~/bin/docker  
  
VOLUME ["$HOME/.ivy2", "/src"]  
  
WORKDIR /src  
  
# -l Make bash act as if it had been invoked as a login shell  
# so `which docker` return ~/bin/docker  
CMD bash -l  

