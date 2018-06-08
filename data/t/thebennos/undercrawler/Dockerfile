FROM thebennos/omm-arach-base  
  
WORKDIR /undercrawler  
  
COPY requirements.txt .  
RUN pip install -r requirements.txt && \  
formasaurus init  
COPY . .  
RUN pip install -e .  
ADD ./arachnado.conf /etc/arachnado.conf  
CMD ["arachnado"]  

