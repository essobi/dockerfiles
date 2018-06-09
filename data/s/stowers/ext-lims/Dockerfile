FROM ubuntu:16.04  
#  
# Packages and dependencies  
#  
RUN echo "Installing Packages..." \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
build-essential \  
default-jre \  
git \  
libfontconfig \  
ruby \  
ruby-dev \  
unzip \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean all \  
&& echo "DONE"  
  
# Create user to run webserver and shell commands as  
# These need to be the same because the web app requires writable access to
many  
# directories  
RUN useradd --create-home --uid 5000 --shell /bin/bash limsuser && \  
usermod --lock limsuser && \  
chown -R limsuser:limsuser /home/limsuser/  
  
#  
# Sencha CMD 6.2  
#  
# compass requires: build-essential libfontconfig ruby ruby-dev  
#  
ARG SenchaVersion=6.2.2  
RUN echo "Installing Sencha Cmd..." && \  
gem install compass  
  
USER limsuser  
ENV HOME /home/limsuser  
  
COPY resources/cmd-install-responsefile /tmp/cmd-install-responsefile  
RUN wget -O $HOME/cmd-install.run.zip
http://cdn.sencha.com/cmd/${SenchaVersion}/no-
jre/SenchaCmd-${SenchaVersion}-linux-amd64.sh.zip && \  
unzip -p $HOME/cmd-install.run.zip > $HOME/cmd-install.run && \  
chmod +x $HOME/cmd-install.run && \  
INSTALL4J_ADD_VM_PARAMS="-Djava.awt.headless=true" $HOME/cmd-install.run -q
-varfile /tmp/cmd-install-responsefile && \  
echo "export PATH=$PATH:/home/limsuser/bin/Sencha/Cmd/" >> $HOME/.bash_profile
&& \  
rm \  
$HOME/cmd-install.run.zip \  
$HOME/cmd-install.run && \  
chown -R limsuser:limsuser /home/limsuser/bin && \  
echo "DONE"  
  
USER root  
  
COPY resources/root/docker-entrypoint.sh /root/  
COPY resources/usr/local/bin/dockerlims-shell /usr/local/bin/  
  
WORKDIR /var/www/html/Ext  
  
# NOTE: must use json syntax to ensure process is not started in a subshell
(and signals are passed correctly)  
ENTRYPOINT ["/root/docker-entrypoint.sh"]  

