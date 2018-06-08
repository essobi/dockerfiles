FROM joshendriks/walletbase  
  
ENV GIT_COIN_URL https://github.com/rapidpayc/rapid.git  
ENV GIT_COIN_NAME rapid  
  
RUN apt-get update \  
&& apt-get -y install wget \  
&& wget https://github.com/rapidpayc/rapid/releases/download/v1.0.0/rapid-
linux64-cli-v1.0.0.tar.gz \  
&& tar -zxvf rapid-linux64-cli-v1.0.0.tar.gz \  
&& rm rapid-linux64-cli-v1.0.0.tar.gz  
  
RUN apt-get install -y git virtualenv python-virtualenv cron nano \  
&& cd / && git clone https://github.com/rapidpayc/sentinel.git sentinel \  
&& cd sentinel && virtualenv venv && venv/bin/pip install -r requirements.txt
\  
&& sed -i "s/database\/sentinel.db/\/sentinel\/database\/sentinel.db/g"
/sentinel/sentinel.conf \  
&& echo "* * * * * /sentinel.sh >> /data/sentinel.log 2>&1" | crontab -u root
-  
  
#Add a config so you can run without providing a bitnodes.conf through a
volume  
COPY rapid.conf /data/.rapidcore/rapid.conf  
COPY sentinel.sh /sentinel.sh  
RUN chmod 777 /sentinel.sh  
  
EXPOSE 4528 4527  
ENV HOME /data  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
CMD /start.sh

