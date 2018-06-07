FROM alpine:edge  
MAINTAINER Matt Lehman <dmlehman99 at homtmail.com>  
  
RUN apk update && \  
apk add git bash supervisor nodejs ca-certificates wget apache2 php5
php5-mysql mysql && \  
apk add pwgen php5-apache2 php5-mcrypt supervisor && \  
mkdir -p /app/gruyere && \  
adduser -S -s /bin/false -D -H app app  
  
WORKDIR /app  
  
# install DVNA and DVWA  
RUN git clone https://github.com/quantumfoam/dvna.git  
  
WORKDIR /app/dvna  
  
RUN npm set progress=false && npm install  
  
WORKDIR /app/gruyere  
  
RUN wget -O gruyere-code.zip http://google-gruyere.appspot.com/gruyere-
code.zip && \  
unzip gruyere-code.zip && \  
rm gruyere-code.zip && \  
sed -i 's/insecure_mode = False/insecure_mode = True/' gruyere.py && \  
sed -i 's/request_ip = self.client_address\\[0\\]/request_ip = "127.0.0.1"/'
gruyere.py && \  
chown -R app /app  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD sysctl.conf /etc/sysctl.conf  
  
EXPOSE 3000 8008  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

