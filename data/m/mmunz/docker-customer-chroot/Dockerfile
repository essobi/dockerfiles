FROM debian:stable-slim  
# install packages  
RUN apt-get update && apt-get install \--no-install-recommends -y nano vim
vim-scripts git rsync \  
mariadb-client socat wget curl patch less ssh-client ca-certificates bzip2
file xz-utils vim-addon-manager \  
php-cli php-bcmath php-bz2 php-curl php-gd php-gmp php-json php-mbstring \  
php-mysql php-opcache php-readline php-soap php-sqlite3 php-xml php-zip zip
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# remove unneeded and potentially unsecure binaries  
RUN find / -type f -perm -4000 ! -path "/proc/*" -exec chmod -s {} \; \  
&& for f in \  
/bin/mount /usr/bin/chage /usr/bin/chfn /usr/bin/chsh /usr/bin/gpasswd
/usr/bin/passwd \  
/usr/sbin/chgpasswd /usr/sbin/chpasswd /usr/sbin/cpgr /usr/sbin/cppw
/usr/sbin/groupadd \  
/usr/sbin/groupdel /usr/sbin/groupmems /usr/sbin/groupmod /usr/sbin/grpck
/usr/sbin/grpconv \  
/usr/sbin/grpunconv /usr/sbin/newusers /usr/sbin/pwck /usr/sbin/pwconv
/usr/sbin/pwunconv \  
/usr/sbin/useradd /usr/sbin/userdel /usr/sbin/usermod /usr/sbin/vigr
/usr/sbin/vipw \  
/usr/bin/faillog /usr/bin/lastlog /usr/bin/newgrp /usr/bin/sg
/usr/sbin/update-passwd \  
/usr/sbin/addgroup /usr/sbin/adduser /usr/sbin/delgroup /usr/sbin/deluser \  
/bin/mount /bin/umount /sbin/losetup /sbin/swapoff /sbin/swapon; \  
do rm -rf $f; done  

