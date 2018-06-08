FROM debian  
  
USER root  
  
ENV TERM xterm  
  
RUN apt-get update && \  
apt-get -qy install git-core php5-cli php5-common php5-gd php5-mcrypt php-pear
libncursesw5-dev php5-dev make && \  
apt-get clean  
  
RUN pecl install ncurses  
  
ENV HOME /home/slacker  
  
WORKDIR $HOME  
  
RUN git clone https://github.com/TidalLabs/Slacker.git && \  
cd $HOME/Slacker && make install  
  
RUN cp $HOME/Slacker/slacker.php /usr/local/bin/slacker && \  
chmod a+x /usr/local/bin/slacker  
  
RUN echo "extension=ncurses.so" >> /etc/php5/cli/php.ini  
  
RUN sed -e '/^[^;]*allow_url_fopen/s/=.*$/= On/' -i.bak /etc/php5/cli/php.ini  
RUN sed -e '/^[^;]*allow_url_include/s/=.*$/= On/' -i.bak
/etc/php5/cli/php.ini  
  
CMD ["slacker"]  

