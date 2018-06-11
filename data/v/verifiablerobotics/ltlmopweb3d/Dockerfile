FROM agilgur5/ltlmop:web  
MAINTAINER agilgur5  
  
# install python requirements  
WORKDIR /web  
COPY ./requirements.txt ./requirements.txt  
RUN pip -q install -r requirements.txt  
  
# add the production code to the image  
COPY ./ /web  
  
# expose dev server port  
EXPOSE 5000  
CMD python application.py  

