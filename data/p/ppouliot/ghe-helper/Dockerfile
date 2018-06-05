FROM alpine:latest  
MAINTAINER peter@pouliot.net  
  
ADD VERSION .  
ENV GHE_VERSION 0.0.5  
ENV JENKINS_VERSION 3.16  
ENV JENKINS_CLI_VERSION 3.16  
ENV PYPY_VERSION pypy3-v5.10.1-linux64  
  
USER root  
ENV HOME /root  
RUN \  
apk add --no-cache \  
git wget curl rsync openssh \  
bash openssh-server vim \  
expect screen byobu \  
sudo ruby ruby-dev g++ \  
gcc make bison bzip2 ca-certificates \  
libffi-dev gdbm-dev openssl-dev yaml-dev \  
python3 python3-dev jq build-base \  
openjdk8-jre libbz2 sqlite-dev procps zlib-dev \  
ruby-irb ruby-rake ruby-io-console \  
ruby-bigdecimal ruby-json ruby-bundler \  
libstdc++ tzdata bash ca-certificates \  
linux-headers icu-dev libxml2-dev libxslt-dev \  
&& echo 'gem: --no-document' > /etc/gemrc  
  
RUN \  
ln -s `which python3` /usr/local/bin/python \  
&& ln -s `which pip3` /usr/local/bin/pip \  
&& pip3 install argparse setuptools future jenkins-job-builder keyrings.alt
Pygments stashy python-gitlab \  
# To install from a release  
# && pip3 install https://git.generalassemb.ly/ga-admin-
utils/ghe/releases/download/${GHE_VERSION}/ghe-${GHE_VERSION}.tar.gz  
# To install directly from git  
# && pip3 install git+https://git.generalassemb.ly/ga-admin-utils/ghe.git  
# Installing downstream with some bug fixes.  
&& pip3 install git+https://github.com/ppouliot/ghe.git  
  
RUN echo "*** Installing Gems required for GH-Pages/jekyll and GH-Wiki/gollum
***"  
RUN gem install bundler github-pages jekyll \  
rouge jekyll-redirect-from kramdown rdiscount \  
sinatra gollum github-markdown redcarpet \  
org-ruby rdoc rake bitbucket_rest_api  
  
RUN \  
echo "*** Enabling Byobu for Startup of GHE-Helper Services ***" \  
byobu-enable \  
byobu-enable-prompt  
  
RUN byobu-ctrl-a screen \  
byobu-janitor  
  
COPY byobu/windows.tmux /root/.byobu/windows.tmux  
COPY byobu/.tmux.conf /root/.byobu/.tmux.conf  
COPY byobu/statusrc /usr/share/byobu/status/statusrc  
  
RUN \  
echo "*** Installing GitHub Backup Utils to /usr/github-backup-utils ***" \  
&& git clone -b stable https://github.com/github/backup-utils /usr/github-
backup-utils \  
&& mkdir -p /etc/github-backup-utils/ \  
&& echo "*** Installing GitHub Platform Samples to /opt/github-platform-
samples ***" \  
&& git clone https://github.com/github/platform-samples github-platform-
samples \  
&& sed -i 's/PATH=/PATH=\/usr\/github-backup-utils\/bin\:/g' /etc/profile \  
&& sed -i 's/\\\h/\\\u\@\\\h/g' /etc/profile  
  
COPY etc/github-backup-utils/backup.config /etc/github-backup-utils/  
RUN adduser -D gh-pages -h /home/gh-pages -s /bin/bash \  
&& echo "gh-pages:gh-pages" | chpasswd \  
&& echo "gh-pages ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& adduser -D gh-backup -h /home/gh-backup -s /bin/bash \  
&& echo "gh-backup:gh-backup" | chpasswd \  
&& echo "gh-backup ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
ENV HOME /home/gh-pages  
USER gh-pages  
WORKDIR $HOME  
RUN echo "*** Creating GH/GHE wiki/pages src directories ***" \  
&& mkdir -p wiki pages  
  
ENV HOME /home/gh-backup  
USER gh-backup  
WORKDIR $HOME  
RUN \  
echo "*** Installing GitHub Backup Utils ***" \  
&& mkdir bin  
  
ENV PATH "/usr/github-backup-utils/bin:${PATH}"  
ENV HOME /root  
USER root  
WORKDIR $HOME  
COPY Dockerfile /Dockerfile  
COPY etc/motd /etc/motd  
COPY bin/* /usr/local/bin/  
VOLUME /data  
CMD byobu  
EXPOSE 4000 4567  

