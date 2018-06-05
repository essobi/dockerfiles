FROM python:3.6.1-onbuild  
# Install polyglot dependencies  
RUN apt-get update && apt-get install -y python-numpy libicu-dev  
  
# Install supplemental dependencies  
RUN pip install PyICU==2.0.3  
  
# Install french language for Polyglot  
RUN sh setup_post_requirements.sh  
  
CMD ["python", "analyze_podcasts.py"]

