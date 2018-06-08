FROM finalduty/archlinux  
MAINTAINER Michal Kimle <kimle.michal@gmail.com>  
  
ENV NIFTY_VERSION 0.2.12  
# update + dependencies  
RUN pacman -Syu --noconfirm && pacman -S --noconfirm wget git base-devel
openssh  
  
# install ruby-2.3.3  
RUN wget
https://archive.archlinux.org/packages/r/ruby/ruby-2.3.3-2-x86_64.pkg.tar.xz
&& pacman -U --noconfirm ruby-*-x86_64.pkg.tar.xz  
  
# nifty  
RUN gem install nifty -v $NIFTY_VERSION  
  
# ruby gems access  
ENV PATH=$PATH:/root/.gem/ruby/2.3.0/bin  
  
ENTRYPOINT ["nifty"]  

