FROM python:3.6  
LABEL maintainer "Michael Hahn <mhahn.dev@gmail.com>"  
  
RUN rm /dev/random && ln -s /dev/urandom /dev/random  
  
ENV CONTAINER_USERNAME dummy  
ENV CONTAINER_GROUPNAME dummy  
ENV HOMEDIR /home/dummy  
  
RUN groupadd -f -g $(id -g) dummy && useradd -g dummy dummy && mkdir --parent
$HOMEDIR && chown -R dummy:dummy $HOMEDIR  
  
WORKDIR $HOMEDIR/app  
  
# Copy the requirements file and install all dependencies  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy all app files  
COPY . .  
  
# Expose the HTTP server port  
EXPOSE 8080  
# Run the app  
CMD su dummy -c 'python -m run'  
  
#  
# Manually build by running:  
#  
# docker build -t trade4chor/hdtapps-framework .  
#  
#  

