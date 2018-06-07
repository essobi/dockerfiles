FROM python:2-alpine  
LABEL maintainer=helder  
  
# Install Flower  
RUN pip install flower  
  
# Expose port 5555 so that we can connect to it  
EXPOSE 5555  
# Run Flower  
CMD ["flower", "--port=5555"]  

