FROM ubuntu:16.04  
LABEL maintainer="Wilmar den Ouden <info@wilmardenouden.nl>"  
  
ENV container docker  
  
RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get upgrade -y &&
apt-get install -y python sudo bash ca-certificates && apt-get clean; \  
elif [ $(command -v dnf) ]; then dnf makecache && dnf --assumeyes install
python sudo python-devel python2-dnf bash && dnf clean all; \  
elif [ $(command -v yum) ]; then yum makecache fast && yum update -y && yum
install -y python sudo yum-plugin-ovl bash && sed -i 's/plugins=0/plugins=1/g'
/etc/yum.conf && yum clean all; \  
elif [ $(command -v zypper) ]; then zypper refresh && zypper update -y &&
zypper install -y python sudo bash python-xml && zypper clean -a; \  
elif [ $(command -v apk) ]; then apk update && apk add --no-cache python sudo
bash ca-certificates; fi  
  
RUN test -d /run/systemd/system || mkdir /run/systemd/system  
  
COPY systemctl.py /usr/bin/systemctl  
  
CMD /usr/bin/systemctl

