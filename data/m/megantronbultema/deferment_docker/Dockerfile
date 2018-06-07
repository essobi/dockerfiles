# Use an official Python runtime as a parent image  
FROM continuumio/anaconda3  
  
# Set the working directory to /app  
WORKDIR /run  
  
# Copy the current directory contents into the container at /app  
ADD . /run  
  
# Install any needed packages specified in requirements.txt  
RUN conda update -y --all  
#RUN conda update libgcc  
RUN apt-get install -y build-essential  
RUN apt-get update -y  
RUN apt-get install apt-transport-https -y  
RUN apt-get install apt-utils -y  
#RUN wget https://gallery.technet.microsoft.com/ODBC-Driver-13-for-
Ubuntu-b87369f0/file/154097/2/installodbc.sh  
#RUN sh installodbc.sh  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/debian/8/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
RUN apt-get update -y  
RUN ACCEPT_EULA=Y apt-get install msodbcsql -y  
RUN ACCEPT_EULA=Y apt-get install mssql-tools -y  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
#RUN export DEBIAN_FRONTEND = noninteractive  
RUN apt-get install -y locales  
RUN echo 'en_US.UTF-a UTF-a' > /etc/locale.gen  
RUN locale-gen  
RUN update-locale  
#RUN source ~/.bashrc  
RUN apt-get install -y build-essential  
RUN git clone git://github.com/jcrudy/py-earth.git && cd py-earth && python
setup.py install  
  
# Run app.py when the container launches  
CMD ["python", "sql_interface_docker2.py"]  
  
# Set proxy server, replace host:port with values for your servers  
ENV http_proxy http://amrbasic-proxy.bp.com:80  
ENV https_proxy https://amrbasic-proxy.bp.com:80  

