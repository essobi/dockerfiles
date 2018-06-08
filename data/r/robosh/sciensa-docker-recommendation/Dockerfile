# start from miniconda image  
FROM continuumio/miniconda3  
  
# update conda  
RUN conda update -y conda  
  
# add user  
RUN useradd flask-user -G staff -m -s /bin/bash  
WORKDIR /home/flask-user  
  
# Install entrypoint  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
RUN chown -R flask-user:flask-user /usr/bin/entrypoint.sh  
  
# expose port  
EXPOSE 5000  
# define entrypoint  
ENTRYPOINT ["su", "-c", "/usr/bin/entrypoint.sh", "flask-user"]  
CMD []

