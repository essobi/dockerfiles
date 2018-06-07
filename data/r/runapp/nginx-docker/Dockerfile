FROM opensuse:42.3  
MAINTAINER Ben Ma <runappz@gmail.com>  
  
ENV ROOT_PWD=barfoo1!  
  
COPY run.sh /  
RUN chmod +x /run.sh && \  
zypper up -y && \  
zypper in -y openssh wget curl mtr tar vim rzsz && \  
wget https://build.opensuse.org/projects/home:runapp/public_key && \  
rpm --import public_key && \  
rm public_key && \  
zypper in -y
http://download.opensuse.org/repositories/home:/runapp/openSUSE_Leap_42.3/x86_64/nginx-1.13.9-3.1.x86_64.rpm
&& \  
for i in rsa dsa ecdsa ed25519; do ssh-keygen -t $i -N '' -f
/etc/ssh/ssh_host_${i}_key;done && \  
rm -r /var/cache && \  
echo "root:$ROOT_PWD" | chpasswd && \  
true  
  
COPY nginx.conf /etc/nginx/nginx.conf  
#COPY ssh_host_* /etc/ssh/  
EXPOSE 80  
EXPOSE 22  
ENTRYPOINT ["/run.sh"]  
  

