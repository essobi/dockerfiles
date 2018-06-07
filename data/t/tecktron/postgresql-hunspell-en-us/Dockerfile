FROM postgres:9.6  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y hunspell-en-us \  
&& rm -rf /var/lib/apt/lists/*  
  
# update the dictionary files.  
RUN /usr/sbin/pg_updatedicts  
  
# hunspell uses a "en_us" file naming convention (which differs from the
packaged sample version)  
# since the samples were removed anyway, lets adjust the links back to the
"english" file name.  
RUN mv /usr/share/postgresql/$PG_MAJOR/tsearch_data/en_us.dict
/usr/share/postgresql/$PG_MAJOR/tsearch_data/english.dict  
RUN mv /usr/share/postgresql/$PG_MAJOR/tsearch_data/en_us.affix
/usr/share/postgresql/$PG_MAJOR/tsearch_data/english.affix  
  
# We need to reload the server for the dictionaries to take effect  
RUN /etc/init.d/postgresql reload  

