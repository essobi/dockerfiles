from ubuntu:latest  
  
env DEBIAN_FRONTEND noninteractive  
  
# Enable "extra" users, this makes  
# overlaying our passwd/shadow/group content easier  
run echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >>
/etc/apt/sources.list  
run apt-get update  
run apt-get install -y libnss-extrausers  
run sed -i '/^\\(passwd\|group\|shadow\\):/{ s/$/ extrausers/; }'
/etc/nsswitch.conf  
  
# Install samba!  
run apt-get install -y samba  
  
# Make directories for shared paths  
run mkdir -p /mnt/shared  
run mkdir -p /mnt/guest  
  
expose 445  
expose 139  
expose 135  
# Add user management tool  
add docker-smb-user /usr/local/bin/  
  
entrypoint ["/usr/sbin/smbd"]  
cmd ["-F", "-S"]  

