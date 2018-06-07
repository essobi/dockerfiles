FROM felixkazuyade/baseimage  
MAINTAINER Felix Kazyua  
  
# Umgebungsvariablen  
ENV ROOT_PASSWORD ChangeMeByEnv  
ENV UBUNTU_PASSWORD ChangeMeByEnv  
  
  
#Date of Build  
RUN echo "Built at" $(date) > /etc/built_at  
  
# Portfreigaben  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
# Dateien reinkopieren  
ADD entrypoint /entrypoint  
  
#Konfiguration  
RUN useradd -ms /bin/bash ubuntu  
RUN adduser ubuntu sudo  
  
# Anwendungen  
RUN apt-get update  
RUN apt-get update && apt-get install -y openssh-server git git-crypt ansible
zsh tmux dialog apt-utils sudo  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/PermitRootLogin PermitRootLogin prohibit-
password/PermitRootLogin yes/' /etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN chsh -s $(which zsh); sh -c "$(curl -fsSL
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"; exit 0;  
  
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
CMD ["/entrypoint"]

