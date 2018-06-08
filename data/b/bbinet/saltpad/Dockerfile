FROM debian:wheezy  
  
MAINTAINER Bruno Binet <bruno.binet@helioslite.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yq --no-install-recommends python-pip \  
git ca-certificates  
RUN pip install futures gunicorn jinja2 flask flask-wtf requests werkzeug  
  
RUN git clone https://github.com/tinyclues/saltpad.git /root/saltpad  
ENV PYTHONPATH /root/saltpad  
ENV SALTPAD_VERSION a66449b38c816ae3a35e1e61d06ce550fa7d51eb  
RUN git --git-dir /root/saltpad/.git --work-tree=/root/saltpad reset --hard
${SALTPAD_VERSION}  
  
VOLUME ["/root/saltpad/saltpad/local_settings.py"]  
VOLUME ["/etc/pki/tls/certs"]  
  
EXPOSE 443  
CMD ["gunicorn", "--bind=0.0.0.0:443", "--threads=2", "--
certfile=/etc/pki/tls/certs/server.crt", "--
keyfile=/etc/pki/tls/certs/server.key", "--chdir=/root/saltpad/saltpad",
"saltpad.app:app"]  

