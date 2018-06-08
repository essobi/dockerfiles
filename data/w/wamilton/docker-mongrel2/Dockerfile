FROM ubuntu  
  
RUN apt-get -qq -y update && apt-get -q -y install curl build-essential
sqlite3 libsqlite3-dev uuid-dev  
RUN curl -L http://download.zeromq.org/zeromq-2.1.4.tar.gz | tar xz && cd
zero* && ./configure && make && make install  
RUN ldconfig -v  
RUN curl -L https://github.com/zedshaw/mongrel2/archive/v1.8.1.tar.gz | tar xz
&& cd mongrel* && make install  
ADD mongrel2-start /usr/sbin/mongrel2-start  
RUN mkdir -p /etc/mongrel2/run /etc/mongrel2/logs  
ADD default.conf /etc/mongrel2/default.conf  
RUN chmod 775 /usr/sbin/mongrel2-start  
RUN chown -R www-data /etc/mongrel2  
EXPOSE 8080 9999 9998  
ENTRYPOINT [ "mongrel2-start" ]  
CMD [ "main" ]  

