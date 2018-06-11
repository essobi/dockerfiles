FROM jesselang/debian-vagrant:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RAILS_ENV development  
  
RUN sed -i 's/deb.debian.org/ftp2.de.debian.org/g' /etc/apt/sources.list \  
&& apt-get -qq -o Dpkg::Use-Pty=0 update \  
&& apt-get -qq -o Dpkg::Use-Pty=0 install -y git curl libmysqld-dev
imagemagick libmagickwand-dev \  
mysql-server memcached redis-server dnsmasq nginx apt-transport-https gnupg2
mysql-server-5.5 \  
&& echo "address=/yogaeasy.de/127.0.0.1" > /etc/dnsmasq.d/yogaeasy.conf \  
&& echo >> /etc/dnsmasq.conf \  
&& echo "user=root" >> /etc/dnsmasq.conf \  
&& sed '1s/^/nameserver 127.0.0.1\n/g' /etc/resolv.conf > ~/resolv.conf \  
&& cp -f ~/resolv.conf /etc/resolv.conf \  
&& rm -f ~/resolv.conf \  
&& apt-get -qq install -y dirmngr gnupg \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7 \  
&& apt-get -qq -o Dpkg::Use-Pty=0 install -y ca-certificates \  
&& echo 'deb https://oss-binaries.phusionpassenger.com/apt/passenger jessie
main' > /etc/apt/sources.list.d/passenger.list \  
&& apt-get -qq -o Dpkg::Use-Pty=0 update \  
&& apt-get -qq -o Dpkg::Use-Pty=0 install -y nginx-extras passenger \  
&& sed -i 's/# include \/etc\/nginx\/passenger.conf;/include
\/etc\/nginx\/passenger.conf;/g' /etc/nginx/nginx.conf \  
&& echo "\n\  
server { \n\  
listen 8080;\n\  
server_name _;\n\  
# Tell Nginx and Passenger where your app's 'public' directory is\n\  
root /vagrant/public;\n\  
# Turn on Passenger\n\  
passenger_enabled on;\n\  
passenger_ruby /home/vagrant/.rvm/gems/ruby-2.2.2/wrappers/ruby;\n\  
passenger_app_env ${RAILS_ENV};\n\  
passenger_sticky_sessions on;\n\  
passenger_sticky_sessions_cookie_name _pr;\n\  
passenger_min_instances 4;\n\  
}" >>/etc/nginx/sites-available/yogaeasy.conf \  
&& cd /etc/nginx/sites-enabled \  
&& ln -s ../sites-available/yogaeasy.conf yogaeasy.conf \  
&& mkdir /vagrant \  
&& chown vagrant.vagrant /vagrant \  
&& echo "\n\  
cd /vagrant \n\  
gpg2 --keyserver keyserver.ubuntu.com --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \n\  
curl -sSL https://get.rvm.io | bash -s stable \n\  
echo 'source /home/vagrant/.rvm/scripts/rvm' >> /home/vagrant/.bashrc \n\  
source /home/vagrant/.rvm/scripts/rvm \n\  
rvm install "ruby-2.2.2" \n\  
gem install bundler \n\  
bundle config git.allow_insecure true" | sudo -u vagrant bash  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

