FROM mikafouenski/debian-mono  
MAINTAINER mikafouenski  
  
ENV XDG_CONFIG_HOME="/config/xdg"  
  
ADD maxpeers.patch /  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt install -y \--no-install-recommends git nodejs yarn patch && \  
git clone https://github.com/lidarr/Lidarr.git \--recursive \--depth 1 && \  
cd Lidarr && \  
patch src/NzbDrone.Core/DecisionEngine/DownloadDecisionComparer.cs
/maxpeers.patch && \  
./build.sh && \  
cp -a _output_linux /opt/Lidarr && \  
yarn cache clean && \  
apt remove -y git nodejs yarn patch && \  
apt autoremove -y && \  
rm -rf /maxpeers.patch /root/* /Lidarr /tmp/* /var/lib/apt/lists/* /var/tmp/*
/var/cache/*  
  
COPY root/ /  
  
EXPOSE 8686  
VOLUME /config /downloads /music  

