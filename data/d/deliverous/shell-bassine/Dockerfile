FROM deliverous/common-bassine  
  
# pour marketing : rails + test avec webrick  
RUN apt-get update \  
&& apt-get install -y \  
qt4-dev-tools \  
qt4-qmake \  
ruby \  
&& apt-get clean \  
&& gem install bundle  
  
# Pour l'api en go  
RUN apt-get update \  
&& apt-get install -y \  
golang \  
vim-gocomplete \  
gocode-auto-complete-el \  
&& apt-get clean  
  
# Pour le site azae  
RUN apt-get update \  
&& apt-get install -y jekyll \  
&& apt-get clean  
  
# Pour le blog deliverous  
RUN apt-get update \  
&& apt-get install -y pelican \  
&& apt-get clean  
  
USER pierre  
RUN echo "[ -f ~/workspace/bin/env.sh ] && source ~/workspace/bin/env.sh" >>
/home/pierre/.bashrc  
RUN vim-addon-manager install go-syntax dockerfile  
  
USER root  
  
ADD get-deliverous /usr/local/bin/get-deliverous  
RUN chmod 755 /usr/local/bin/get-deliverous  
  
ADD authorized_keys /home/pierre/.ssh/authorized_keys  
RUN chown -R pierre:pierre /home/pierre/ \  
&& chmod 600 /home/pierre/.ssh/authorized_keys  
  
RUN git clone https://github.com/mnagel/clustergit /usr/local/src/clustergit \  
&& ln -s /usr/local/src/clustergit/clustergit /usr/local/bin/clustergit  
RUN git clone https://github.com/StreakyCobra/gws /usr/local/src/gws \  
&& ln -s /usr/local/src/gws/src/gws /usr/local/bin/gws  
  
# Pour ansible  
RUN apt-get update \  
&& apt-get install -y \  
python-dev \  
python-pip \  
python-setuptools \  
&& apt-get clean \  
&& pip install ansible  
  
VOLUME ["/home/pierre/workspace", "/home/pierre/native"]  
EXPOSE 22 8000  
CMD ["/usr/sbin/sshd", "-D"]  

