  
FROM vertigo/dev-base  
  
ARG BASEREPO  
ARG EPELREPO  
  
RUN sh /opt/setbaserepo.sh && \  
sh /opt/setepelrepo.sh && \  
yum install openssh-server openssh-clients passwd sudo -y && \  
yum clean all  
  
ENV USERPWD secret  
ENV PUBLICKEY ""  
ENV PUBLICROOTKEY ""  
ENV KEYONLY false  
  
ADD src/*.sh /opt/  
  
RUN useradd -u 5001 -G users -m user && \  
echo "$USERPWD" | passwd user --stdin && \  
chmod +x /opt/*.sh && \  
sh /opt/generatekeys.sh && \  
sed -i '/^session.*pam_loginuid.so/s/^session/# session/' /etc/pam.d/sshd && \  
sed -i 's/Defaults.*requiretty/#Defaults requiretty/g' /etc/sudoers  
  
# copy zsh env and carina tools  
RUN cp /root/.zshrc ~user/.zshrc && \  
cp /root/.bashrc ~user/.bashrc && \  
cp -R /root/.oh-my-zsh ~user/ && \  
cp -R /root/.dvm ~user/ && \  
cp -R /root/bin ~user/ && \  
chown -R user:user ~user/  
  
# passwordless sudo  
ADD src/user /etc/sudoers.d/user  
  
EXPOSE 22  
CMD ["/opt/startsshd.sh"]  

