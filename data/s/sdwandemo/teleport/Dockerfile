FROM voobscout/base-arch:latest  
MAINTAINER Voobscout <voobscout@archlinux.info>  
  
RUN runuser -l dev \  
-c 'yaourt -Syy --noconfirm --needed \  
go \  
zip && \  
mkdir -p $HOME/go/src/github.com/gravitational && \  
cd $HOME/go/src/github.com/gravitational && \  
curl -L https://github.com/gravitational/teleport/archive/v2.2.4.tar.gz | tar
xvz && \  
mv teleport-2.2.4 teleport && \  
cd $HOME/go/src/github.com/gravitational/teleport && \  
make release && \  
cd build && \  
sudo install -m755 -t "/usr/bin/" teleport tctl tsh && \  
cd && \  
rm -rf $HOME/go' && \  
pacman -Rsc --noconfirm zip go  
  
EXPOSE 3022 3023 3024 3025 3080  
  
VOLUME ["/var/lib/teleport"]  
CMD ["/usr/bin/teleport"]  

