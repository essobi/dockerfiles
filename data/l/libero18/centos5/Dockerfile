FROM libero18/base:centos5.11  
#  
MAINTAINER NAKAJIMA, Ryuichi (a.k.a. libero18)  
  
# 環境変数  
ENV PATH $PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
# パッケージアップデート＆インストール  
RUN yum -y install yum-fastestmirror ;\  
yum -y update ;\  
yum -y install --enablerepo=centosplus openssl-devel libselinux-python
libselinux-utils libselinux ;\  
yum -y install openssh openssh-server openssh-clients sudo python-simplejson
curl ;\  
yum -y clean all  
  
# セキュリティ設定  
RUN sed -i "s/^#auth\t\trequired\tpam_wheel.so
use_uid/auth\t\trequired\tpam_wheel.so use_uid/g" /etc/pam.d/su ;\  
echo -e "## Read drop-in files from /etc/sudoers.d (the # here does not mean a
comment)\n#includedir /etc/sudoers.d\n\nDefaults secure_path =
/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin\n" >>
/etc/sudoers ;\  
sed -i "s/^Defaults requiretty$/Defaults:%provisioner \\!requiretty/g"
/etc/sudoers ;\  
test -d /etc/sudoers.d || mkdir /etc/sudoers.d ;\  
chmod 755 /etc/sudoers.d ;\  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/wheel ;\  
chmod 440 /etc/sudoers.d/wheel ;\  
sed -i "s/^UsePAM\s*yes/\\#UsePAM yes/g" /etc/ssh/sshd_config ;\  
sed -i "s/^\\#UsePAM\s*no/UsePAM no/g" /etc/ssh/sshd_config ;\  
sed -i "s/^\\#RSAAuthentication\s*yes/&\\\nRSAAuthentication yes/g"
/etc/ssh/sshd_config ;\  
sed -i "s/^\\#PubkeyAuthentication\s*yes/&\\\nPubkeyAuthentication yes/g"
/etc/ssh/sshd_config ;\  
sed -i
"s/^\\#AuthorizedKeysFile\s*\\.ssh\/authorized_keys/&\\\nAuthorizedKeysFile
\\.ssh\/authorized_keys/g" /etc/ssh/sshd_config  
  
# ユーザ作成  
RUN useradd -G wheel -m provisioner ;\  
sudo -u provisioner mkdir /home/provisioner/.ssh ;\  
chmod 700 /home/provisioner/.ssh ;\  
sudo -u provisioner sh -c 'echo -e \  
"ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDoWQ+FBk37HxX02it/6NJXN2HeBDIeo3HNT+M7O2pKVaPzU1riJg8O3BZdWc87CesFdK6T43GzA2+P2dD2mkwb9qnXiSb+D9F15xdvFK0BlWz+AppPW3LH6+Lf5Hdnm8z0hzYu8bADFDQMArva1fFEKl1mTki2WK8M7RID9nxrPH6/o5JnlyNF/ISw6MnYCDVc4pQW8zPcdwf3wz6XLOHO+wZ7tZSzM4asp1r2d5EfXe0psXrr4eM2WtNNj9Vcj2870hjQ0SZfxt0GlqnpMSUeUpLSBhlyTrM1Ckvw/X1EnCzdBOlbaejM+81c/A9O4l79pIwPA9IHCHFVE1q/n82r\nssh-
rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDipySiPabQpTC2NfxYuY43yqX3dDscw5+4LjrZ3sP+SSKYRZD8Htj/wBtdL+/a040yCHjgwNXn7V8RFib5wpl7GM3ItgbONN7IWXvgU34xXeJuPzfxX2KGRm6nzMWQpRKlAd7/JUu1IPY38huWv5a5FEaFjWzBUotW+pwhbGzesOIZOKfGycHOrJf6/WnqtnSC/MyelVGFIrU3Cwn3HvnOBM+hgK7KzbpHbPKP//YKMOSPzCGJgHvA/ke6XzNwS2cj0RjA1FMVu7s2Xw/zEGGhrc6P+QF1Dxv2ssQUviL5blbu/zW2NmOEN5eMz9n6JUx8W81fE7lCm2X5UMu/VDI5"
\  
> /home/provisioner/.ssh/authorized_keys' ;\  
chmod 600 /home/provisioner/.ssh/authorized_keys  
  
# sshd設定  
RUN service sshd start ;\  
service sshd stop  
  
# ポート開放  
EXPOSE 22  
# コンテナ起動時に自動実行されるコマンドを指定  
CMD ["/usr/sbin/sshd", "-D"]  
  

