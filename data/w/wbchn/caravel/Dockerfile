FROM python:2.7.10  
# Install caravel  
RUN pip install caravel  
  
# Create an admin user env  
ENV username admin  
ENV password changeme  
ENV firstname admin  
ENV lastname sample  
ENV email user@sample.com  
  
# Add server script and default config  
ADD run.sh /run.sh  
ADD caravel/* /caravel/  
  
EXPOSE 8088  
# Start the web server foreground  
CMD [ "/bin/bash", "/run.sh" ]  

