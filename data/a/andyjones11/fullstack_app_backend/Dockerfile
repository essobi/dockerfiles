FROM python:3.5-alpine  
  
ENV PYTHONUNBUFFERED 1  
RUN apk add --no-cache supervisor netcat-openbsd postgresql-dev gcc
python3-dev musl-dev  
  
# make directory to store all backend files  
RUN mkdir /backend  
WORKDIR /backend  
  
# copy all the stuff in backend folder on the host into the backend folder in
the container  
COPY . backend/  
  
# make the run_server script executable  
RUN chmod +x backend/_tooling/run_server.sh  
  
EXPOSE 5000  
# copy and install python requirements  
RUN pip install --upgrade pip \  
&& pip install -r backend/requirements.txt \  
&& rm backend/requirements.txt  
  
CMD ["/backend/_tooling/run_server.sh"]  
  

