FROM node:4.5.0-wheezy  
  
ADD . /app  
WORKDIR /app  
RUN apt-get update  
RUN useradd -d /home/term -m -s /bin/bash term  
RUN echo 'term:term' | chpasswd  
  
RUN npm install && openssl req -x509 -newkey rsa:4096 -keyout sprutio.key -out
sprutio.csr -days 365 -nodes -subj "/C=RU/O=Beget/CN=sprut.io"  
  
EXPOSE 3000  
ENTRYPOINT ["node"]  
CMD ["app.js", "--sslkey", "sprutio.key", "--sslcert", "sprutio.csr", "-p",
"3000"]

