FROM frolvlad/alpine-python3  
RUN apk add --no-cache gcc python3-dev build-base && pip install virtualenv &&
mkdir -p /app  
WORKDIR /app  
RUN virtualenv /env && /env/bin/pip3 install 'wheel>=0.26.0' && /env/bin/pip3
install 'pyzmq>=15.1.0'  
COPY . /app  
RUN /env/bin/pip3 install -r /app/requirements.txt  
CMD [ "/env/bin/python3", "./temperature_sender.py" ]  

