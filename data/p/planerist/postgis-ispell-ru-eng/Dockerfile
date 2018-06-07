#install rus & en ispell dictionaries  
FROM mdillon/postgis  
  
COPY dict/en_us.affix /usr/share/postgresql/9.4/tsearch_data/english.affix  
COPY dict/en_us.dict /usr/share/postgresql/9.4/tsearch_data/english.dict  
  
COPY dict/russian.affix /usr/share/postgresql/9.4/tsearch_data/russian.affix  
COPY dict/russian.dict /usr/share/postgresql/9.4/tsearch_data/russian.dict

