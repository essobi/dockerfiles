FROM felixkazuyade/worksuite  
MAINTAINER Felix Kazyua  
  
# Umgebungsvariablen  
ENV ROOT_PASSWORD ChangeMeByEnv  
ENV UBUNTU_PASSWORD ChangeMeByEnv  
ENV DEBIAN_FRONTEND noninteractive  
  
  
#Date of Build  
RUN echo "Built at" $(date) > /etc/built_at  
  
# Portfreigaben  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3389  
# Dateien reinkopieren  
ADD entrypoint /entrypoint  
ADD supervisor.conf /etc/supervisor/conf.d/xrdp.conf  
  
#Konfiguration  
# Anwendungen  
RUN apt-get -yq install xfce4  
RUN apt-get -yq install xrdp  
RUN apt-get -yq install xfce4-goodies  
RUN apt-get -yq install lxde  
RUN apt-get -yq install lxdm  
RUN apt-get -yq install apt-transport-https  
  
RUN xrdp-keygen xrdp auto  
RUN echo 'pgrep -U $(id -u) lxsession | grep -v ^$_LXSESSION_PID | xargs --no-
run-if-empty kill' > /bin/lxcleanup.sh  
RUN chmod +x /bin/lxcleanup.sh  
RUN echo '@lxcleanup.sh' >> /etc/xdg/lxsession/LXDE/autostart  
  
RUN wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | apt-key
add -  
RUN echo "deb https://download.sublimetext.com/ apt/stable/" | tee
/etc/apt/sources.list.d/sublime-text.list  
RUN apt-get update  
RUN apt-get install sublime-text  
  
RUN apt-get clean  
  
#Specific User stuff  
USER ubuntu  
WORKDIR /home/ubuntu  
RUN echo xfce4-session > /home/ubuntu/.xsession  
RUN chsh -s $(which zsh); sh -c "$(curl -fsSL
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"; exit 0;  
USER root  
  
# Startbefehl  
# Combining ENTRYPOINT and CMD allows you to specify the default executable
for your image while also providing default arguments to that executable which
may be overridden by the user.  
# When both an ENTRYPOINT and CMD are specified, the CMD string(s) will be
appended to the ENTRYPOINT in order to generate the container's command
string. Remember that the CMD value can be easily overridden by supplying one
or more arguments to `docker run` after the name of the image.  
# Entrypoint explizit override needed  
# Entrypoint needs new value for each argument ["/bin/ping","-c","4"]  
# CMD Overwrite by arguments after run (same as Entrypoint ["localhost"])  
RUN chmod +x /entrypoint  
CMD ["supervisord", "-n"]  

