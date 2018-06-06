FROM python:2.7.10  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash  
RUN apt-get install -y nodejs  
  
ADD package.json ./package.json  
RUN npm install  
  
ADD requirements.txt ./requirements.txt  
RUN pip install -r requirements.txt  
  
ADD BackendlessClient.py ./BackendlessClient.py  
ADD OneSignalClient.py ./OneSignalClient.py  
ADD petharbor_kingcounty.py ./petharbor_kingcounty.py  
ADD craigslist_seattle.py ./craigslist_seattle.py  
ADD romps.py ./romps.py  
  
ADD run.sh ./run.sh  
  
CMD ["./run.sh"]

