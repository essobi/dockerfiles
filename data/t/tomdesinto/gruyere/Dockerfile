FROM python:2  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update &&\  
apt-get -y install unzip &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /gruyere &&\  
curl http://google-gruyere.appspot.com/gruyere-code.zip > /gruyere/gruyere-
code.zip &&\  
cd /gruyere &&\  
unzip gruyere-code.zip &&\  
rm gruyere-code.zip &&\  
sed -i 's/insecure_mode = False/insecure_mode = True/' /gruyere/gruyere.py &&\  
sed -i 's/request_ip = self.client_address\\[0\\]/request_ip = "127.0.0.1"/'
/gruyere/gruyere.py  
  
WORKDIR /gruyere  
EXPOSE 8008  
CMD ["python", "gruyere.py"]

