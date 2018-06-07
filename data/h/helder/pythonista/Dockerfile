FROM ikalnitsky/pythonista  
  
RUN pip install -U pip  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
ca-certificates mysql-client libmysqlclient-dev gcc gettext && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

