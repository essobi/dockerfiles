# docker run -d --name=tmux-server -p 7000:22 -v $PWD/home:/home
pdxjohnny/tmuxserver  
# docker exec -ti tmux-server adduser -s /bin/bash $USER  
# docker exec -ti tmux-server sed -i "s/.*host_list=.*/host_list=($USER)/g"
/usr/local/etc/wemux.conf  
FROM alpine:3.3  
RUN apk --no-cache add \  
openssh \  
tmux \  
bash \  
vim \  
git && \  
ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \  
ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa && \  
git clone https://github.com/zolrath/wemux.git /usr/local/share/wemux && \  
mkdir -p /usr/local/bin /usr/local/etc && \  
ln -s /usr/local/share/wemux/wemux /usr/local/bin/wemux && \  
cp /usr/local/share/wemux/wemux.conf.example /usr/local/etc/wemux.conf && \  
adduser -S -s /bin/bash wemux && \  
sed -i "s/.*host_list=.*/host_list=(wemux)/g" /usr/local/etc/wemux.conf  
  
COPY startup.sh /bin/init.d/startup.sh  
  
ENTRYPOINT ["/bin/init.d/startup.sh"]  

