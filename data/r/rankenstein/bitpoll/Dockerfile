FROM alpine:3.7  
# dumb-init libldap nodejs postgresql-libs python2 py-flask-script py2-pip
ruby  
RUN apk --no-cache add dumb-init python3 py3-psycopg2 py3-ldap3 gettext
libstdc++ mariadb-client-libs  
  
RUN ln -s python3 /usr/bin/python && ln -s pip3 /usr/bin/pip  
  
# gcc git libffi-dev make musl-dev openldap-dev python2-dev postgresql-dev
ruby-dev ruby-irb ruby-rdoc  
RUN apk --no-cache add --virtual .build-dependencies alpine-sdk gcc g++ git
python3-dev mariadb-dev openldap-dev linux-headers && \  
git clone \--depth=1 https://github.com/fsinfuhh/Bitpoll.git /bitpoll && \  
cd /bitpoll && \  
pip install -r requirements-production.txt && \  
pip install mysqlclient && \  
apk --no-cache del .build-dependencies  
  
COPY ./start.sh /usr/local/bin/  
  
EXPOSE 8888  
WORKDIR /bitpoll  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["sh", "/usr/local/bin/start.sh"]  

