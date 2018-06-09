FROM python:2.7  
MAINTAINER Ingolf Wagner <docker@ingolf-wagner.de>  
  
#  
# install gdom package  
#  
RUN pip install -e 'git+https://github.com/syrusakbary/gdom#egg=gdom'  
  
#  
# patch it  
#  
RUN sed -i 's/app.run\\(\\)/app.run\\(host="0.0.0.0", port=8080\\)/'
/src/gdom/gdom/cmd.py \  
&& sed -i 's/app.debug = True/app.debug = False/' /src/gdom/gdom/cmd.py  
  
EXPOSE 8080  
#  
# run as gdom user  
#  
RUN useradd gdom  
USER gdom  
CMD exec gdom --test  
  

