# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Preakelt Foundation dev@praekelt.com  
  
# Update the sources list  
RUN apt-get update  
  
# Install Python and Basic Python Tools  
RUN apt-get install --no-install-recommends -y curl tar build-essential python
python-dev python-distribute python-pip python-virtualenv postgresql-client
libpq-dev  
RUN apt-get remove -y perl --auto-remove  
  
# Copy the application folder inside the container  
RUN curl -Lso unicoredocker.tar.gz https://github.com/praekelt/unicore-mama-
sbm/tarball/develop/; tar xf unicoredocker.tar.gz; name=$(tar -tzf
unicoredocker.tar.gz | head -n 1); mv $name $(echo $name | cut -d'-' -f 1-4);
rm unicoredocker.tar.gz  
  
#Install dependencies  
WORKDIR /praekelt-unicore-mama-sbm  
RUN cp run.sh /  
RUN virtualenv ve  
RUN ve/bin/pip install -r requirements.pip  
  
WORKDIR /praekelt-unicore-mama-sbm/mamasbm  
  
# Expose ports  
EXPOSE 8000  
# Set the default command to execute  
# when creating a new container  
CMD ../ve/bin/gunicorn --paste production.ini --chdir .  

