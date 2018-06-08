FROM python:3.4  
  
MAINTAINER Alex Barcelo <alex.barcelo@gmail.com>  
  
#########################################################  
# Prepare the user mailman, which will run the commands #  
#########################################################  
# explicitly set user/group IDs  
RUN groupadd -r mailman --gid=999 && useradd -r -g mailman --uid=999 mailman  
  
# grab gosu for easy step-down from root  
RUN curl -L -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu  
  
# Fake the postmap binary, but remember that the host must update the postmap
itself  
RUN cp `which true` /usr/sbin/postmap  
  
########################################  
# Proceed to prepare the mailman stuff #  
########################################  
RUN mkdir /opt/mailman  
  
# Install some extras required for psycopg2 (Postgres Python wrapper)  
RUN apt-get update && apt-get install -y \  
postgresql-client libpq-dev \  
gcc \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
# Python requirements  
COPY requirements.txt /  
RUN pip install --no-cache-dir -r /requirements.txt  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME ["/opt/mailman/var"]  
  
  
ENV POSTGRES_USER postgres  
ENV POSTGRES_PASSWORD postgres  
ENV POSTGRES_DB mailman  
ENV POSTGRES_HOST postgres  
ENV POSTGRES_PORT 5432  
  
ENV MAILMAN_ADMIN_USER mailman  
ENV MAILMAN_ADMIN_PASSWORD mailman  
ENV MAILMAN_HOST_FOR_POSTFIX mailman  
  
ENV POSTFIX_HOST postfix  
ENV POSTFIX_PORT 25  
  
ENV HYPERKITTY_HOST hyperkitty  
ENV HYPERKITTY_PORT 8000  
ENV HYPERKITTY_ARCHIVER_API_KEY hyperkitty  
ENV HYPERKITTY_ENABLE yes  
  
EXPOSE 8024  
EXPOSE 8001  
CMD ["start"]  

