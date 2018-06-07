FROM java:jdk  
MAINTAINER "Nathaniel Rankin Webb" <nrwebb@live.com>  
  
ENV HOME /opt/jetbrains/teamcity  
ENV VERSION 9.1.4  
ENV TAR TeamCity-${VERSION}.tar.gz  
  
WORKDIR $HOME  
RUN wget --progress bar:force:noscroll
https://download.jetbrains.com/teamcity/$TAR && \  
tar -xzf $TAR && \  
mv TeamCity/* $HOME && \  
rmdir TeamCity && \  
rm $TAR  
  
VOLUME ["$HOME", "/root/.BuildServer"]  
EXPOSE 8111  
ENTRYPOINT ["bin/teamcity-server.sh"]  
CMD ["run"]  

