#Tryton Compiler  
FROM ubuntu:latest  
  
RUN mkdir /code  
WORKDIR /code  
#Basic packages  
RUN apt update  
RUN apt install -y python-pip rsync mercurial git  
  
#Package requirement  
RUN apt install -y libcairo2 python-gobject libpango1.0-0  
RUN pip install --upgrade pip setuptools virtualenv wheel botocore boto3 pyaml  
  
#Adding ssh keys  
RUN mkdir -p ~/.ssh/ && touch ~/.ssh/known_hosts  
RUN echo "pypi.calidae.net ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQCfra56MIUw6W2j2DEGBqMLAtFjVNOpnu7ZTqQA2oB8PvRrNjAkJ1o1nTeYDCd3DIKBqshNvYHiSsLSFK5eLA5wP8kPplHMu9eB7FL0E1aJi5u6ePj34zJSpdG8dcmWPXQGjONCgCORDbJQZ8sBpTjpls5AT39zHp49MtjiDOjDjwKSCrBrHbLzFfijfANQ2bx4GgbJ7Secy77xRimru9UCF1CSocJ1nWvTw5JqDz3mClMYbTjxGpUzQ29Nk3fTduqRk1MH7BBJ/vBTDZelF7UZ53nsDVfTAHMz/iQv4jcSpeeg1Rt8HARMTlwD1TcPkH+7wADUX4/9uP2Mla9IDuGD"
>> ~/.ssh/known_hosts  
RUN ssh-keyscan -t rsa bitbucket.org >> ~/.ssh/known_hosts

