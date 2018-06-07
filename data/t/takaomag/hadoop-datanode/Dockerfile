# hadoop-datanode  
  
FROM takaomag/hadoop:release-2.8.1-2017.08.07.07.13  
  
ENV \  
X_DOCKER_REPO_NAME=hadoop-datanode  
  
RUN \  
echo "2016-03-08-0" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 \--verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
  
echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}" &&
\  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
  
cd /etc/supervisor.d && \  
ln -sf hadoop/hdfs-datanode.ini . && \  
ln -sf sshd/sshd.ini . && \  
  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  
EXPOSE \  
22 \  
50010 \  
1004 \  
50075 \  
1006 \  
50020  
#ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--
configuration=/etc/supervisord.conf"]  
ENTRYPOINT ["/opt/local/bin/x-start_hdfs-datanode.sh"]  
  

