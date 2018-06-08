FROM ubuntu:14.04  
MAINTAINER Gergely Risko <errge@nilcons.com>  
RUN useradd -m -g users ox ; groupadd -r wheel ; adduser ox wheel  
RUN echo "%wheel ALL=(ALL:ALL) NOPASSWD: ALL" >>/etc/sudoers  
  
USER ox  
WORKDIR /home/ox  
RUN sudo apt-get install -y emacs24-nox  
  
ADD ox-reveal.patch /home/ox/  
  
RUN sudo apt-get install -y wget make patch && \  
wget https://raw.githubusercontent.com/yjwen/org-
reveal/c4b66bafff6165b39cbe570f4efbecb0572f0e77/ox-reveal.el && \  
patch -p0 <ox-reveal.patch && \  
wget http://orgmode.org/org-8.2.10.tar.gz && \  
tar xfz org-8.2.10.tar.gz && \  
cd org-8.2.10 && \  
make compile && \  
sudo make install-etc install-lisp && \  
sudo apt-get purge -y wget make patch && \  
sudo apt-get autoremove --purge -y && \  
sudo rm -rf /var/log/alternatives.log /var/log/apt /var/log/dpkg.log && \  
cd .. && rm -rf org-8.2.10 org-8.2.10.tar.gz  
  
ADD packages.el /home/ox/  
RUN emacs --batch -l packages.el  
  
ADD batch.el /home/ox/  
VOLUME /ox  
CMD emacs --batch -l batch.el  

