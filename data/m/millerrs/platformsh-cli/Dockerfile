FROM alpine:3.7  
  
ENV PATH /root/.platformsh/bin:$PATH  
  
RUN apk add --no-cache \  
bash \  
curl \  
git \  
openssh \  
php7 \  
php7-curl \  
php7-ctype \  
php7-json \  
php7-mbstring \  
php7-openssl \  
php7-phar \  
&& touch $HOME/.bash_profile \  
&& curl --silent --show-error https://platform.sh/cli/installer | php \  
&& mkdir $HOME/.ssh \  
&& ssh-keyscan -t rsa ssh.us.platform.sh, git.us.platform.sh >>
$HOME/.ssh/known_hosts  
  
CMD ["platform"]

