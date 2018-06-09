FROM centos:latest  
MAINTAINER arthurkiller "arthur-lee@qq.com"  
# this docker file is used to try building a work environment  
RUN sed -i "s/^tsflags=nodocs//" /etc/yum.conf  
RUN rpm -ivh
http://fr2.rpmfind.net/linux/dag/redhat/el6/en/x86_64/dag/RPMS/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm  
  
# Install development tools  
RUN yum groupinstall -y "Development Tools" && yum install -y cmake  
  
# Install fishshell  
RUN curl -L
http://download.opensuse.org/repositories/shells:fish:release:2/CentOS_7/shells:fish:release:2.repo
\  
-o /etc/yum.repos.d/shells:fish:release:2.repo \  
&& yum install -y fish \  
&& chsh -s /usr/bin/fish root  
  
RUN yum install -y man man-pages cmake make \  
build-essential vim sudo unzip libtool \  
autotools-dev automake autoconf \  
curl tar locales wget python python-dev libxml2-dev libxslt-dev \  
git gcc tmux golang lua \  
openssh-server apt-transport-https ca-certificates  
  
RUN git config --global alias.list "log --graph
--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset'
--abbrev-commit --date=relative"  
RUN git config --global user.email "arthur-lee@qq.com"  
RUN git config --global user.name "arthurkiller@arthur-lee"  
  
RUN cd /root && git clone https://github.com/arthurkiller/VIMrc.git \  
&& cd /root/VIMrc/ && yum install -y python-devel && ./install.sh -init  
RUN git clone https://github.com/tony/tmux-config.git ~/.tmux && ln -s
~/.tmux/.tmux.conf ~/.tmux.conf  
# RUN cd /root/.tmux/ && git submodule init && git submodule update \  
# && cd ~/.tmux/vendor/tmux-mem-cpu-load \ && cmake . && make . && make
install \  
# && tmux source-file ~/.tmux.conf && cp ~/.tmux/vendor/basic-cpu-and-
memory.tmux /usr/local/bin/tmux-mem-cpu-load \  
# && chmod +x /usr/local/bin/tmux-mem-cpu-load  
# I have used others dockerfile and do not know what will take place  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
RUN mkdir /var/run/sshd  
  
RUN yum install -y openssh-server \  
&& sed -i "s/^#PermitRootLogin yes/PermitRootLogin yes/" /etc/ssh/sshd_config
\  
&& ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key  
  
# Set root password to 'arthur'  
RUN echo arthur | passwd root --stdin  
RUN mkdir /root/golang && mkdir /root/golang/src && mkdir /root/golang/bin  
RUN mkdir /root/.config && mkdir /root/.config/fish && touch
/root/.config/fish/config.fish  
RUN echo "set -x GOPATH $HOME/golang" >> /root/.config/fish/config.fish  
RUN echo "set -x PATH $GOPATH/bin $PATH" >> /root/.config/fish/config.fish  
  
#set the time && add alias into profile  
ENV LC_ALL en_US.utf8  
RUN echo 'alias ll="ls -lah --color=auto"' >> /etc/profile  
RUN echo "Asia/shanghai" > /etc/timezone  
RUN cp /usr/share/zoneinfo/PRC /etc/localtime  
  
EXPOSE 22  
#start the sshd server  
CMD ["/usr/sbin/sshd", "-D"]  

