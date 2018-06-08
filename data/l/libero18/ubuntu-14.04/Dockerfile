FROM ubuntu:14.04  
#  
MAINTAINER NAKAJIMA, Ryuichi (a.k.a. libero18)  
  
# 環境変数  
ENV PATH $PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
# パッケージアップデート＆インストール  
RUN apt-get update ;\  
apt-get -y upgrade ;\  
apt-get install -y openssh-server curl  
  
# セキュリティ設定  
RUN sed -i 's/^auth\s*required\s*pam_wheel.so\s*use_uid/auth required
pam_wheel.so root_only group=wheel/g' /etc/pam.d/su ;\  
sed -i "s/^Defaults requiretty$/Defaults:%provisioner \\!requiretty/g"
/etc/sudoers ;\  
test -d /etc/sudoers.d || mkdir /etc/sudoers.d && chmod 755 /etc/sudoers.d ;\  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/wheel ;\  
chmod 440 /etc/sudoers.d/wheel  
  
# ユーザ作成  
RUN addgroup --gid 11 wheel ;\  
usermod -a -G wheel root ;\  
useradd -G wheel -m provisioner ;\  
sudo -u provisioner mkdir /home/provisioner/.ssh ;\  
chmod 700 /home/provisioner/.ssh ;\  
sudo -u provisioner curl https://github.com/libero18.keys -o
/home/provisioner/.ssh/authorized_keys ;\  
chmod 600 /home/provisioner/.ssh/authorized_keys  
  
# sshd設定  
RUN mkdir /var/run/sshd  
  
# ポート開放  
EXPOSE 22  
# コンテナ起動時に自動実行されるコマンドを指定  
CMD ["/usr/sbin/sshd", "-D"]  
  

