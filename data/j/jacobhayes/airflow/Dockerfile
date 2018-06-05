# TAG jacobhayes/airflow:onbuild  
FROM jacobhayes/airflow  
  
# APT Requirements  
ONBUILD COPY apt-requirements.txt .  
ONBUILD RUN apt-get update \  
&& xargs apt-get install -y < apt-requirements.txt \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
# Python Requirements  
ONBUILD COPY requirements.txt .  
ONBUILD RUN pip3 install -r requirements.txt --no-deps --no-cache-dir  

