FROM codenvy/ubuntu_python:2.7  
  
################################## Postgres SQL SETUP
###########################################  
  
USER root  
RUN apt-get update && apt-get -y -q install python-software-properties
software-properties-common \  
&& apt-get -y -q install postgresql-9.3 postgresql-client-9.3 postgresql-
contrib-9.3  
  
USER postgres  
  
RUN /etc/init.d/postgresql start \  
&& psql --command "ALTER USER postgres WITH PASSWORD 'postgres';"  
  
USER root  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  
  
################################## END of Postgres SQL SETUP
#######################################  
  
USER user  
RUN sudo apt-get update  
  
# virtualenv wrapper  
  
RUN mkdir ~/.virtualenv  
ENV WORKON_HOME ~/.virtualenvs  
RUN sudo pip install virtualenvwrapper  
RUN echo "export WORKON_HOME=~/.virtualenvs"  
RUN echo ". /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc  
  
# python dependencies  
RUN sudo apt-get install libpq-dev python-dev libtiff5-dev libjpeg8-dev
zlib1g-dev \  
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk -y  
  
  
# working directory  
WORKDIR /projects  
  
# ports available for running django application  
EXPOSE 8000-8100  
  
# create ssh key # commented because of eclipse che disk space restrictions  
RUN rm -rf ~/ssh/id_rsa* && ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""  
  
  
# restarting postgres sql server  
RUN echo "sudo service postgresql restart" >> ~/.bashrc  
  
# user bash shell  
CMD source ~/.bashrc  
CMD tailf /dev/null  
# entry point not works as expected in eclipse che  
# ENTRYPOINT sudo service postgresql restart && bash  
  
  
  
  

