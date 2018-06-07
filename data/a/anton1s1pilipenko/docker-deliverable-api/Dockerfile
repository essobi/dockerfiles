FROM python:3.6  
RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get
install -y openssl build-essential xorg libssl-dev  
COPY wkhtmltox-0.12.3_linux-generic-amd64.tar.xz wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz  
RUN tar -xJf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && cd wkhtmltox &&
chown root:root bin/wkhtmltopdf && cp -r * /usr/  
  
VOLUME ["/tmp"]  
  
ENV PYTHONPATH $PYTHONPATH:/usr/src/app  
WORKDIR /usr/src/app  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . .  
  
CMD python application.py --path /tmp/deliverable_"${API_PROC_NAME}".sock  

