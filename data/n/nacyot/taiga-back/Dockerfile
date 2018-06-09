FROM python:3.4  
MAINTAINER Hylke Visser <htdvisser@gmail.com>  
  
# Install dependencies  
RUN \  
apt-get update -qq && \  
apt-get install -y netcat wget && \  
rm -rf /var/lib/apt/lists/* && \  
pip install circus gunicorn  
  
# Install taiga-back  
RUN \  
wget https://github.com/taigaio/taiga-back/archive/1.8.0.tar.gz -O
/tmp/1.8.0.tar.gz &&\  
tar xvf /tmp/1.8.0.tar.gz -C /tmp &&\  
mkdir -p /usr/local/taiga &&\  
mv /tmp/taiga-back-1.8.0 /usr/local/taiga/taiga-back &&\  
mkdir /usr/local/taiga/media /usr/local/taiga/static /usr/local/taiga/logs &&
\  
cd /usr/local/taiga/taiga-back && \  
pip install -r requirements.txt && \  
touch /usr/local/taiga/taiga-back/settings/dockerenv.py && \  
touch /usr/local/taiga/circus.ini  
  
RUN \  
useradd -d /usr/local/taiga taiga  
  
RUN pip install taiga-contrib-slack taiga-contrib-ldap-auth ldap3  
  
# Add Taiga Configuration  
ADD ./local.py /usr/local/taiga/taiga-back/settings/local.py  
  
# Configure and Start scripts  
ADD ./configure /usr/local/taiga/configure  
ADD ./start /usr/local/taiga/start  
RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start  
  
RUN ln -sf /dev/stdout /usr/local/taiga/logs/gunicorn.stdout.log &&\  
ln -sf /dev/stderr /usr/local/taiga/logs/gunicorn.stderr.log  
  
VOLUME /usr/local/taiga/media  
VOLUME /usr/local/taiga/static  
VOLUME /usr/local/taiga/logs  
  
ENV LDAP_SERVER ldap://ldap.example.com  
ENV LDAP_DN_FORMAT uid={username},cn=users,dc=example,dc=com  
ENV LDAP_BASE_EMAIL @example.com  
  
EXPOSE 8000  
CMD ["/usr/local/taiga/start"]  

