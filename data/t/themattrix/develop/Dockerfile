FROM ubuntu:15.10  
MAINTAINER Matthew Tardiff <mattrix@gmail.com>  
  
# proper init  
ADD https://github.com/krallin/tini/releases/download/v0.8.4/tini /tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y install \  
python-software-properties \  
software-properties-common \  
&& \  
add-apt-repository -y ppa:ultradvorka/ppa && \  
apt-get update && \  
apt-get -y install \  
iptables \  
ca-certificates \  
lxc \  
apt-transport-https \  
tmux \  
git \  
vim \  
htop \  
socat \  
man \  
ruby \  
ruby-dev \  
bash-completion \  
curl \  
python-pygments \  
python-pip \  
python-dev \  
vim-youcompleteme \  
sshfs \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Change the home directory of the root user to /home  
ENV HOME /home  
ENV USER root  
RUN sed -r -i -e 's@^root:.*@root:x:0:0:root:/home:/bin/bash@' /etc/passwd &&
\  
rm -rf /root  
  
# Store the bash history to its own directory so that we can mount a volume  
# to that location and have the history preserved across sessions.  
ENV HISTFILE /home/.bash_history/history  
  
# Check out a specific commit - this has the advantage of invalidating the  
# cache for this RUN command whenever we want to update this repo.  
RUN git clone https://github.com/themattrix/home.git && \  
cd /home && \  
git checkout e871fd5  
  
# Set locale  
RUN locale-gen en_US.UTF-8 && /usr/sbin/update-locale LANG=en_US.UTF-8  
  
RUN echo 'source ~/.bashrc' >> /home/.bash_profile  
  
RUN gem install travis -v 1.8.0 --no-rdoc --no-ri  
  
# docker-engine: "The open-source application container engine"  
# docker-compose: "Define and run complex applications using Docker"  
# docker-machine: "Machine management for a container-centric world"  
RUN curl -sSL https://get.docker.com/ | sh && \  
curl -L https://github.com/docker/compose/releases/download/1.5.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
curl -L https://github.com/docker/machine/releases/download/v0.5.5/docker-
machine_linux-amd64 > /usr/local/bin/docker-machine && \  
chmod +x /usr/local/bin/docker*  
  
# Fuzzy history utility. Seems nicer than hh.  
RUN git clone https://github.com/junegunn/fzf.git /home/.fzf \  
&& (cd /home/.fzf && git checkout 0.11.1) \  
&& (yes | /home/.fzf/install)  
  
# percol: "adds flavor of interactive filtering to the traditional pipe
concept of UNIX shell"  
# eg: "Useful examples at the command line"  
# thefuck: "Magnificent app which corrects your previous console command"  
RUN pip install percol==0.2.1 eg==0.1.1 thefuck==3.2  
  
ADD https://raw.githubusercontent.com/junegunn/vim-plug/0.8.0/plug.vim \  
/home/.vim/autoload/plug.vim  
  
# Install vim plugins  
RUN vim -u /home/.vim_plug -c 'PlugInstall|q!|q!' > /dev/null  
RUN vam install youcompleteme  
  
# Docker-in-docker: https://github.com/jpetazzo/dind  
ADD wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
CMD ["wrapdocker"]  

