# DESCRIPTION: Run Eclipse (with Perl and Subversive plugins) into a container  
# BUILD: docker build -t flem/eclipse-perl-epic .  
# RUN: mkdir $(pwd)/docker-eclipse-perl-epic  
# docker run -d --name eclipse_perl_epic \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /etc/timezone:/etc/timezone:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -v $(pwd)/docker-eclipse-perl-epic:/home/developer \  
# flem/eclipse-perl-epic  
  
  
FROM flem/eclipse  
MAINTAINER Franck Lemoine <franck.lemoine@flem.fr>  
  
# properly setup debian sources  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV PERL_MM_USE_DEFAULT=1  
  
USER root  
  
RUN buildDeps=' \  
make \  
gcc \  
cpanminus \  
' \  
set -x \  
&& apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& apt-get install -y --no-install-recommends libexpat1-dev libxml2-dev
zlib1g-dev \  
&& apt-get install -y --no-install-recommends libterm-readkey-perl \  
&& cpanm 'AppConfig' \  
&& cpanm 'Crypt::CBC' \  
&& cpanm 'Crypt::Blowfish' \  
&& cpanm 'XML::Parser' \  
&& cpanm 'Frontier::Daemon' \  
&& cpanm 'Mail::Send' \  
&& cpanm 'Mail::Sender' \  
&& cpanm 'Mail::Sendmail' \  
&& cpanm 'Log::Log4perl' \  
&& cpanm 'Log::Dispatch::FileRotate' \  
&& cpanm 'Log::Dispatch::Email::MailSend' \  
&& cpanm 'Log::Dispatch::Email::MailSender' \  
&& cpanm 'Net::FTP::File' \  
&& cpanm 'XML::LibXML' \  
&& cpanm 'Switch' \  
&& /opt/eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/ -installIU
org.eclipse.team.svn.revision.graph.feature.group \  
&& /opt/eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/ -installIU
org.eclipse.team.svn.resource.ignore.rules.jdt.feature.group \  
&& /opt/eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/ -installIU
org.eclipse.team.svn.feature.group \  
&& /opt/eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/,http://www.epic-
ide.org/updates/testing -installIU org.epic.feature.main.feature.group \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& apt-get clean autoclean \  
&& rm -r /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  

