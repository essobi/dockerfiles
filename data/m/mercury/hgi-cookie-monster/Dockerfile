FROM mercury/cookie-monster:latest  
MAINTAINER "C. Monster Esq." <cmonster@sanger.ac.uk>  
  
# Install HGI Cookie Monster implementation  
WORKDIR /cookie-monster  
COPY requirements.txt the_monster.sh ./  
COPY hgicookiemonster ./hgicookiemonster/  
  
RUN pip install -U --force -r requirements.txt  
  
EXPOSE 5000  
ENTRYPOINT ["./the_monster.sh"]  

