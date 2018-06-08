FROM theeren/chromedriver:latest  
  
COPY . /home/theeren/PyCharmProjects/scorely01  
  
WORKDIR /home/theeren/PyCharmProjects/scorely01  
  
RUN pip install virtualenv  
  
RUN /home/theeren/PyCharmProjects/scorely01/install_chromedriver.sh  
  
RUN virtualenv /scorely01  
  
RUN . /scorely01/bin/activate && \  
pip install --upgrade pip && \  
pip install -r requirements.txt  
  
EXPOSE 9200  
EXPOSE 9300  
EXPOSE 3128  
ENTRYPOINT ["/home/theeren/PyCharmProjects/scorely01/run.sh"]

