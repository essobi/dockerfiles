FROM ubuntu:trusty  
MAINTAINER Qiang Li  
  
ENV DEBIAN_FRONTEND noninteractive  
  
####  
#  
RUN apt-get update && apt-get -y install \  
apt-utils \  
build-essential \  
ca-certificates \  
curl \  
dnsutils\  
gtk2-engines-pixbuf \  
imagemagick \  
libblas3gf \  
libcurl4-openssl-dev \  
libfftw3-dev \  
libgconf-2-4 \  
libgtk2.0-0 \  
libicu52 \  
liblapack3gf \  
libnss3 \  
libxml2-dev \  
libxpm4 \  
libxrender1 \  
git \  
psmisc \  
unzip \  
wget \  
x11-apps \  
xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \  
xvfb \  
zip  
  
####  
#Oracle Java 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(lsb_release
-sc) main" >> /etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys EEA14886 \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
oracle-java8-installer \  
oracle-java8-set-default  
  
#Google Chrome  
RUN wget -q -O - http://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
google-chrome-stable  
  
#Node  
RUN echo "deb http://deb.nodesource.com/node_6.x $(lsb_release -sc) main" >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 68576280 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
nodejs  
  
RUN npm install --prefix /usr/local \--unsafe-perm -g \  
protractor \  
protractor-flake \  
\  
child_process \  
express \  
multer \  
url \  
&& npm update \  
&& webdriver-manager clean \  
&& webdriver-manager update --versions.standalone=3.5.0 --versions.chrome=2.31
--ignore_ssl --chrome true \--gecko false \--verbose  
  
#Golang  
RUN curl --insecure -L "https://dl.google.com/go/go1.10.1.linux-amd64.tar.gz"
| tar -C /usr/local -xz  
  
#Cloud Foundry client  
RUN curl --insecure -L
"https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar
-C /usr/local/bin -xz  
  
#R runtime  
RUN git clone https://github.com/asperitus/R.git /opt/R  
  
#Node 6.10.0  
RUN npm install -g n \  
&& n 6.10.0  
  
#Tini  
#https://github.com/docker/docker.github.io/issues/3149  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
#additional  
RUN apt-get update && apt-get -y install \  
sshpass  
  
#sshd  
RUN apt-get update && apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo 'root:nosecret' | chpasswd \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
# SSH login fix. Otherwise user is kicked off after login  
&& sed -i 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' /etc/pam.d/sshd  
  
#  
RUN apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
##  
RUN echo "echo never > /sys/kernel/mm/transparent_hugepage/enabled" >
/etc/rc.local \  
&& chmod a+x /etc/rc.local  
  
#user  
RUN useradd -m -b /home -s /bin/bash vcap \  
&& echo "$LOGIN ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& mkdir -p /home/vcap/app \  
&& mkdir -p /home/vcap/tmp \  
&& chown -R vcap:vcap /home/vcap \  
&& ln -s /home/vcap/app /app  
  
#R  
RUN mkdir -p /home/vcap/app/vendor \  
&& chown vcap:vcap /home/vcap/app/vendor \  
&& ln -s /opt/R /home/vcap/app/vendor  
  
EXPOSE 8080  
####  
USER vcap  
  
ENV PORT 8080  
ENV USER vcap  
ENV HOME /home/vcap/app  
ENV PATH /app/bin:/usr/local/go/bin:/app/vendor/R/bin:$PATH  
ENV TMPDIR /home/vcap/tmp  
  
WORKDIR $HOME  
#  
CMD ["/bin/bash"]  
##

