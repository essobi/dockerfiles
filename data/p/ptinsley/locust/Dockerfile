FROM python:2.7  
COPY setup*.sh /tmp/  
RUN useradd locust && \  
bash /tmp/setup_chromedriver.sh && \  
rm -rf /tmp/*  
  
RUN pip install locustio pyzmq  
  
COPY startup.sh /  
  
EXPOSE 5557 5558 8089  
ENTRYPOINT ["/startup.sh"]  

