FROM ubuntu  
  
RUN \  
# . /etc/lsb-release && \  
# mv /etc/apt/sources.list /etc/apt/sources.list.bak \  
# && echo "deb mirror://mirrors.ubuntu.com/mirrors.txt ${DISTRIB_CODENAME}
main restricted universe multiverse" >/etc/apt/sources.list \  
# && echo "deb mirror://mirrors.ubuntu.com/mirrors.txt
${DISTRIB_CODENAME}-updates main restricted universe multiverse"
>>/etc/apt/sources.list \  
# && echo "deb mirror://mirrors.ubuntu.com/mirrors.txt
${DISTRIB_CODENAME}-backports main restricted universe multiverse"
>>/etc/apt/sources.list \  
# && echo "deb mirror://mirrors.ubuntu.com/mirrors.txt
${DISTRIB_CODENAME}-security main restricted universe multiverse"
>>/etc/apt/sources.list \  
# && cat /etc/apt/sources.list.bak >>/etc/apt/sources.list \  
apt-get update \  
\  
&& echo deb http://dl.bintray.com/basespace/BaseSpaceCLI-DEB trusty main
>/etc/apt/sources.list.d/illumina.list \  
&& echo deb http://dl.bintray.com/basespace/BaseMount-DEB saucy main
>>/etc/apt/sources.list.d/illumina.list \  
&& echo deb http://dl.bintray.com/basespace/BaseSpaceFS-DEB saucy main
>>/etc/apt/sources.list.d/illumina.list \  
\  
&& apt-get install -y curl \  
&& curl "https://bintray.com/user/downloadSubjectPublicKey?username=basespace"
| apt-key add \- \  
\  
&& apt-get update \  
&& apt-get install -y \  
curl \  
basespace-cli \  
basemount -y \  
&& apt-get -o DPkg::options::=--force-confmiss install bsfs -y \  
\  
# && bash -c "$(curl -kL https://basemount.basespace.illumina.com/install)" \  
# && bash -c "$(curl -L
https://bintray.com/artifact/download/basespace/helper/install.sh)"  
\  
&& mkdir -p /basespace /volume /root/.basespace \  
&& chmod 600 /root/.basespace \  
&& ln -s /volume/default.cfg /root/.basespace/ \  
\  
&& echo >/basemount.sh "#!/bin/bash" \  
&& echo >>/basemount.sh basemount /basespace \  
&& echo >>/basemount.sh env '${*:-bash}' \  
&& chmod +x /basemount.sh  
  
VOLUME [ "/volume" ]  
  
ENTRYPOINT [ "/basemount.sh" ]  

