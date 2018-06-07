FROM nginx:1.13.12-alpine  
RUN apk add --no-cache python uwsgi py2-crypto py2-flask py2-setuptools
openssl uwsgi-python  
RUN openssl req -x509 -newkey rsa:2048 -keyout /etc/nginx/key.pem -out
/etc/nginx/cert.pem -subj "/CN=test.example.com" -nodes  
COPY . /d-note/  
WORKDIR /d-note  
RUN ["/usr/bin/python", "setup.py", "install"]  
RUN mkdir /etc/dnote && mkdir -p /var/lib/dnote/data && cp d-note.ini
/etc/dnote/d-note.ini  
RUN ["/usr/bin/python", "scripts/generate_dnote_hashes"]  
RUN apk del --no-cache py2-pip openssl  
COPY nginx.conf /etc/nginx/conf.d/default.conf  
ENV FLASK_APP=/d-note/dnote/__init__.py  
CMD nginx && uwsgi --ini uwsgi.ini  

