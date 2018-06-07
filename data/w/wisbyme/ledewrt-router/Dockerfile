FROM ubuntu:17.10  
  
LABEL maintainer="kenlea <kenlea@163.com>"  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Ledewrt Builder" \  
org.label-schema.description="Ledewrt 固件交叉编译环境" \  
org.label-schema.url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vendor="kenlea" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENV FORCE_UNSAFE_CONFIGURE 1  
  
COPY buildenv_ledewrt.sh /root/buildenv_ledewrt.sh  
COPY download_ledewrt.sh /root/download_ledewrt.sh  
  
COPY R7800/config_all_r7800 /root/config_all_r7800  
COPY R7800/4.4_qcom-ipq8065-r7800.dts /root/4.4_qcom-ipq8065-r7800.dts  
COPY R7800/4.9_qcom-ipq8065-r7800.dts /root/4.9_qcom-ipq8065-r7800.dts  
COPY R7800/make_r7800.sh /root/make_r7800.sh  
COPY R7800/commit_r7800.sh /root/commit_r7800.sh  
COPY R7800/update_r7800.sh /root/update_r7800.sh  
  
COPY PUBLICssh/id_rsa /root/id_rsa  
COPY PUBLICssh/id_rsa.pub /root/id_rsa.pub  
COPY PUBLICssh/known_hosts /root/known_hosts  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update -y \  
&& apt-get install -y \  
sudo net-tools cron e2fsprogs wget vim openssl curl psmisc git \  
heirloom-mailx autoconf automake bison bzip2 bsdtar diffutils sed file flex
g++ libslang2 \  
gawk gcc-multilib gettext gperf groff-base zsh libncurses5-dev libexpat1-dev
libelf-dev \  
libssl-dev libtool libtool-bin libxml-parser-perl make patch perl pkg-config
python \  
shtool tar texinfo unzip zlib1g zlib1g-dev intltool autopoint libltdl-dev
libelf1 \  
gengetopt mtd-utils sharutils u-boot-tools libstdc++5 xsltproc dos2unix
tofrodos \  
device-tree-compiler gitk cmake autogen qemu asciidoc \  
subversion p7zip p7zip-full \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& rm -rf /var/cache/apt/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /home/LEDEWRT/tmp /root/R7800 /root/.ssh \  
&& mv /root/commit_r7800.sh /root/R7800 \  
&& mv /root/make_r7800.sh /root/R7800 \  
&& mv /root/update_r7800.sh /root/R7800 \  
&& mv /root/4.4_qcom-ipq8065-r7800.dts /root/R7800 \  
&& mv /root/4.9_qcom-ipq8065-r7800.dts /root/R7800 \  
&& mv /root/config_all_r7800 /root/R7800 \  
&& mv /root/id_rsa /root/.ssh/ \  
&& mv /root/id_rsa.pub /root/.ssh/ \  
&& mv /root/known_hosts /root/.ssh/ \  
&& chmod +x /root/*.sh \  
&& chmod +x /root/R7800/*.sh \  
&& chmod 600 /root/.ssh/* \  
&& git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& echo ". ~/buildenv_ledewrt.sh" >> /root/.zshrc \  
&& chsh -s /bin/zsh \  
&& cd /home/LEDEWRT \  
&& /root/download_ledewrt.sh  
  
CMD ["zsh"]  
WORKDIR /home/LEDEWRT  

