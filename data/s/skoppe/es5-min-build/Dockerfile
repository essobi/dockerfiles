FROM greyltc/archlinux  
  
MAINTAINER Sebastiaan Koppe <mail@skoppe.eu>  
  
RUN pacman --noconfirm -Sy --force dub dmd nginx php-fpm libevent git && \  
# Clean up to make this as small as possible  
# Remove info, man and docs  
rm -r /usr/share/info/* && \  
rm -r /usr/share/man/* && \  
  
# Delete any backup files like /etc/pacman.d/gnupg/pubring.gpg~  
find /. -name "*~" -type f -delete && \  
  
# Clean up pacman  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/* && \  
# install phantomjs  
curl -LO
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar xfj phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /bin/ && \  
rm -rf phantomjs-2.1.1-linux-x86_64 && \  
rm phantomjs-2.1.1-linux-x86_64.tar.bz2  
  
ADD nginx.conf /etc/nginx/nginx.conf  

