FROM kopppcappp/archlinux-yaourt  
MAINTAINER Mikhail Belyaev  
  
RUN pacman -Syy  
RUN pacman --noconfirm --needed -S postgresql  
RUN sudo -u postgres initdb --locale en_US.UTF-8 -E UTF8 -D
"/var/lib/postgres/data"  
  
RUN sudo mkdir /run/postgresql  
RUN sudo chown postgres:postgres /run/postgresql  
RUN sudo -u postgres /usr/bin/postgresql-check-db-dir "/var/lib/postgres/data"  
COPY start_postgresql.sh /usr/bin/start_postgresql.sh  
RUN sudo chmod +s /usr/bin/start_postgresql.sh  
RUN sudo chmod +x /usr/bin/start_postgresql.sh  
RUN pacman --noconfirm --needed -S git  
RUN pacman --noconfirm --needed -S mercurial  
RUN sudo -u yaourt yaourt --noconfirm --needed -S jdk  
RUN pacman --noconfirm --needed -S maven  
RUN sudo -u yaourt yaourt --noconfirm --needed -S teamcity  
COPY start_teamcity.sh /usr/bin/start_teamcity.sh  
RUN sudo chmod +s /usr/bin/start_teamcity.sh  
RUN sudo chmod +x /usr/bin/start_teamcity.sh  
RUN hg clone https://bitbucket.org/vorpal-research/kotoed && \  
cd kotoed && \  
mvn -pl kotoed-js install && \  
mvn dependency:resolve dependency:resolve-plugins  
RUN rm -rf kotoed  
COPY BuildServer.tar.gz /root/  
RUN cd /root && tar xpvzf BuildServer.tar.gz  
  
RUN true  
  
RUN pacman --noconfirm -S python-virtualenv  
RUN hg clone https://bitbucket.org/vorpal-research/kotoed-buildbot-deploy
/root/hg/kotoed-buildbot-deploy  
RUN bash /root/hg/kotoed-buildbot-deploy/deploy-buildbot.sh /root/buildbot
kotoed-worker kotoed-password  

