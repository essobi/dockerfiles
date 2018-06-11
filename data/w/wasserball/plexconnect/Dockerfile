FROM python:2.7  
# https://github.com/iBaa/PlexConnect  
# Installation  
RUN git clone https://github.com/iBaa/PlexConnect.git  
WORKDIR /PlexConnect  
RUN ls  
# Updating  
RUN git pull  
  
# ADD certificates  
COPY certificates assets/certificates  
  
# Run  
CMD ["python", "PlexConnect.py"]  
  
EXPOSE 80 443  
# docker build -t wasserball/plexconnect:latest .  
# docker push wasserball/plexconnect:latest  

