FROM ubuntu:14.04.2  
MAINTAINER alateam <team@ala-it.com>  
  
##################### 常用文件夹准备  
RUN mkdir /workspace /tools /runner /temp  
ENV DEBIAN_FRONTEND noninteractive  
  
  
##################### 更新系统  
RUN apt-get update  
  
###########ADD safe user  
RUN useradd -m -u 600 safe  
  
  
############### 安装ssh server  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:ala' | chpasswd  
EXPOSE 22  
# CMD ["/usr/sbin/sshd", "-D"]  
  
  
##################### 常用工具  
RUN apt-get -y install gcc make build-essential curl wget vim openssl unzip
python git mysql-client python-pip  
  
##################### install oh-my-zsh  
RUN apt-get -y install zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh  
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc  
RUN chsh -s /bin/zsh  
  
##############install nvm  
ENV HOME /root  
ENV PATH /root/.nvm/v0.10.36/bin:$PATH  
RUN git clone https://github.com/creationix/nvm.git $HOME/.nvm  
RUN pwd $HOME/.nvm/  
  
  
##############install node  
RUN bash -c '. $HOME/.nvm/nvm.sh; nvm install 0.10.36 && nvm alias default
0.10.36'  
#########install pm2  
Run npm install pm2 -g  
  
############install sqlite3  
RUn apt-get install -y sqlite3  
  
############install php  
RUN apt-get -y install php5-fpm php5-cli php5-mysql php5-mcrypt php5-gd php-
pear php-apc php5-curl php5-sqlite  
RUN php5enmod mcrypt  
  
  
############install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
  
  
###########install shadowsocks  
RUN pip install shadowsocks  
  
  
###########install shadowsocks  
  
RUN cd /temp && git clone https://github.com/rofl0r/proxychains-ng.git  
  
WORKDIR /temp/proxychains-ng  
RUN ./configure --prefix=/usr --sysconfdir=/etc && make install && make
install-config  
  
  
  
  
  

