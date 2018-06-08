FROM alpine  
RUN apk add --no-cache git python3 texinfo  
RUN git clone https://github.com/erkin/ponysay.git; \  
cd ponysay; \  
python3 setup.py install --freedom=partial; \  
cd /; \  
rm -fr ponysay  

