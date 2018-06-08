FROM ubuntu:latest  
RUN apt-get update -y && apt-get install -y python-pip supervisor git  
RUN apt-get install -y wget  
WORKDIR /app  
  
RUN pip install uwsgi flask==0.10.1 flask-login==0.2.6  
RUN pip install requests  
  
# Clone and configure the orca-web interface  
RUN git clone https://github.com/theorcaproject/orca-web.git  
COPY orca-web-config.wsgi /app/orca-web-config.wsgi  
COPY orca-web-uwsgi.ini /app/orca-web-uwsgi.ini  
COPY supervisorctl-app.conf /etc/supervisor/conf.d/  
  
# Clone and build the orca trainer  
RUN wget https://storage.googleapis.com/golang/go1.10.1.linux-amd64.tar.gz  
RUN tar -xvf go1.10.1.linux-amd64.tar.gz  
RUN mv go /usr/local  
RUN export GOROOT=/usr/local/go  
  
ENV GOROOT=/usr/local/go  
ENV GOPATH=/app/build  
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH  
RUN mkdir /app/build && mkdir /app/build/src  
  
RUN cd /app/build/src && git clone https://github.com/theorcaproject/orca.git  
RUN go get orca/trainer  
RUN go build orca/trainer  
RUN go install orca/trainer  
  
# Install mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list  
RUN apt-get update && apt-get install -y mongodb-org  
  
# Build me a new image plz, and now for realz -  
EXPOSE 8080 5001 5002  
CMD ["supervisord", "-n"]  

