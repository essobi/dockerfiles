# The MIT License (MIT)  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade  
RUN apt-get -y install php7.0 php7.0-fpm php7.0-xml php7.0-gd php7.0-json
php7.0-mbstring php7.0-soap php7.0-zip php7.0-opcache php7.0-curl php7.0-mysql
php-redis php7.0-mcrypt php-xdebug poppler-utils php7.0-imap  
  
RUN php -r "readfile('https://packagecloud.io/gpg.key');" | apt-key add -  
RUN echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
RUN apt-get update && apt-get install blackfire-php  
RUN mkdir /var/log/php/ && mkdir /run/php/  
  
COPY conf /  
  
# Create a user to match the GUID of our user  
# TODO A better solution is required because machines may have multiple users  
RUN useradd application  
  
EXPOSE 9000  
ENTRYPOINT ["php-fpm7.0", "--nodaemonize"]

