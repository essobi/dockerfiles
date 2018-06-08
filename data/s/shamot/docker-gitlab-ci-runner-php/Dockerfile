FROM ubuntu:16.04  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-
init_1.0.2_amd64 /usr/bin/dumb-init  
RUN chmod +x /usr/bin/dumb-init  
  
RUN apt-get update -y && apt-get install -y software-properties-common  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y ca-certificates wget apt-transport-https vim nano \  
curl php7.2 php7.2-cli php7.2-json php7.2-sqlite git php7.2-intl php7.2-imap \  
php-xdebug php7.2-curl php7.2-mbstring php-xml php7.2-soap php7.2-gd unzip &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-
runner/script.deb.sh | bash  
  
RUN echo $'Explanation: Prefer GitLab provided packages over the Debian native
ones\n\  
Package: gitlab-runner\n\  
Pin: origin packages.gitlab.com\n\  
Pin-Priority: 1001' > /etc/apt/preferences.d/pin-gitlab-runner.pref  
  
RUN apt-get update -y && \  
apt-get install -y gitlab-runner && \  
wget -q https://github.com/docker/machine/releases/download/v0.7.0/docker-
machine-Linux-x86_64 -O /usr/bin/docker-machine && \  
chmod +x /usr/bin/docker-machine && \  
apt-get clean && \  
mkdir -p /etc/gitlab-runner/certs && \  
chmod -R 700 /etc/gitlab-runner && \  
rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint /  
RUN chmod +x /entrypoint  
  
VOLUME ["/etc/gitlab-runner", "/home/gitlab-runner"]  
ENTRYPOINT ["/usr/bin/dumb-init", "/entrypoint"]  
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  

