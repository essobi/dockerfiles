FROM node:latest  
COPY pgdq.list /etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add \- \  
&& apt-get update  
RUN apt-get update \  
&& apt-get install -y postgresql-9.5 postgresql-contrib-9.5 \  
&& apt-get install sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# copy working ph_hba.conf with trust for localhost connection_string  
COPY pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf  

