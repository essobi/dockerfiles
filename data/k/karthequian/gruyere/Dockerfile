FROM gliderlabs/alpine:3.3  
MAINTAINER Karthik Gaekwad  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
curl \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /gruyere &&\  
curl http://google-gruyere.appspot.com/gruyere-code.zip > /gruyere/gruyere-
code.zip &&\  
cd /gruyere &&\  
unzip gruyere-code.zip &&\  
rm gruyere-code.zip &&\  
sed -i 's/insecure_mode = False/insecure_mode = True/' /gruyere/gruyere.py &&\  
sed -i "s/_Exit('bad_id')/#_Exit('bad_id')/" /gruyere/gruyere.py &&\  
sed -i 's/request_ip = self.client_address\\[0\\]/request_ip = "127.0.0.1"/'
/gruyere/gruyere.py  
  
WORKDIR /gruyere  
EXPOSE 8008  
CMD ["python", "gruyere.py"]

