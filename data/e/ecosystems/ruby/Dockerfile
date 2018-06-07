FROM base/devel  
MAINTAINER joe@joefiorini.com  
  
RUN pacman -Syy && pacman -S --noconfirm reflector && reflector --verbose -l
200 -p http --sort rate --save /etc/pacman.d/mirrorlist  
  
ADD pkglist.txt /root/pkglist.txt  
RUN pacman -S --noconfirm $(< /root/pkglist.txt)  
  
ADD ruby-2.0.0-p481.tar.gz /src  
WORKDIR /src/ruby-2.0.0-p481  
  
RUN ./configure && make && make install  
  
WORKDIR /  
  
RUN rm -rf /src/ruby-2.0.0-p481  
  
ENV PATH $PATH:/.gem/ruby/2.0.0/bin  
RUN gem install bundler rails  
  

