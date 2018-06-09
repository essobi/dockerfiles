FROM python:3.6  
RUN apt update && apt upgrade -y && apt autoremove -y && apt clean -y  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask uWSGI requests redis  
COPY app /app  
COPY cmd.sh /  
RUN chmod +x cmd.sh  
EXPOSE 5000 9090 9191  
USER uwsgi  
# WORKDIR /app  
CMD [ "./cmd.sh" ]  

