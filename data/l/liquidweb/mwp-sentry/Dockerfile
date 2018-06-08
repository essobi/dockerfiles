  
############################################################  
# Dockerfile to set up Sentry  
############################################################  
  
# Set the base image to sentry  
FROM sentry:8.7  
  
RUN pip install sentry-slack  
  
CMD ["sentry django migrate && sentry start"]  

