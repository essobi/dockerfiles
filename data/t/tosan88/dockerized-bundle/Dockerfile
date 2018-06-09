FROM ubuntu:16.04  
  
RUN /bin/bash -c "apt-get update && apt-get install -y \  
curl \  
net-tools && \  
# Installing XAMPP  
curl \"https://downloadsapachefriends.global.ssl.fastly.net/xampp-
files/7.0.15/xampp-linux-x64-7.0.15-0-installer.run?from_af=true\" -o xampp-
linux-x64-7.0.15-0-installer.run && \  
chmod 755 xampp-linux-x64-7.0.15-0-installer.run && \  
./xampp-linux-x64-7.0.15-0-installer.run && \  
# Installing Ruby with Sass  
gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
curl -sSL https://get.rvm.io | bash -s stable --ruby --gems=sass"  

