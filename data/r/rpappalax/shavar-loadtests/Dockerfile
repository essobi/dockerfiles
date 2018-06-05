# Mozilla Load-Tester  
FROM python:3.5-slim  
  
RUN apt-get update -y; \  
pip3 install https://github.com/loads/molotov/archive/master.zip; \  
pip3 install querystringsafe_base64==0.2.0; \  
pip3 install six; \  
apt-get install -y wget;  
  
WORKDIR /molotov  
ADD . /molotov  
  
CMD molotov -c $VERBOSE -d $TEST_DURATION -w $TEST_CONNECTIONS loadtest.py  

