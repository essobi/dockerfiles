#  
# PHP School  
# A revolutionary new way to learn PHP.  
# Bring your imagination to life in an open learning eco-system.  
# http://phpschool.io  
#  
FROM php:7-cli  
LABEL authors="Michael Woodward <mikeymike.mw@gmail.com>, Aydin Hassan
<aydin@hotmail.com>, Rafael Corrêa Gomes <rafaelcg_stz@hotmail.com>, Shaun
Hare <http://shaunhare.co.uk/>"  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-utils \  
zip \  
git \  
vim \  
libzip-dev \  
zlib1g-dev \  
&& docker-php-ext-configure zip --with-zlib-dir=/usr \  
&& docker-php-ext-install -j$(nproc) zip  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir /phpschool  
  
ENV PATH /root/.php-school/bin/:$PATH  
  
# Workshop manager  
RUN curl -O https://php-school.github.io/workshop-manager/workshop-
manager.phar \  
&& mv workshop-manager.phar /usr/local/bin/workshop-manager \  
&& chmod +x /usr/local/bin/workshop-manager \  
&& workshop-manager verify  
  
WORKDIR /phpschool  
  
# Learn You PHP!  
RUN workshop-manager install learnyouphp  
  
# Callable Functions  
RUN workshop-manager install callablefunctions  
  
# PHP7 Way  
RUN workshop-manager install php7way  
  
CMD ["bash"]  

