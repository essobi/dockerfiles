FROM openaustralia/mapit  
MAINTAINER Matthew Landauer <matthew@oaf.org.au>  
  
# There are two alternate ways to add the data. The first is to download it
locally using "make download"  
# and then insert the files here  
# ADD data /data  
# The second way is to insert the files directly.  
ADD
http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&1259030001_ste11aaust_shape.zip&1259.0.30.001&Data%20Cubes&D39E28B23F39F498CA2578CC00120E25&0&July%202011&14.07.2011&Latest
data/STE11aAust.zip  
ADD http://aec.gov.au/Electorates/gis/files/national-esri-16122011.zip
data/COM20111216_ELB_region.zip  
ADD
http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_poa_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&71B4572D909B934ECA2578D40012FE0D&0&July%202011&22.07.2011&Previous
data/POA_2011_AUST.zip  
ADD
http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_sed_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&1F692001AC7E460DCA2578D40013567C&0&July%202011&22.07.2011&Previous
data/SED_2011_AUST.zip  
ADD
http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_lga_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&4A320EE17A293459CA257937000CC967&0&July%202011&31.10.2011&Previous
data/LGA_2011_AUST.zip  
ADD
http://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055003_ced_2011_aust_shape.zip&1270.0.55.003&Data%20Cubes&AFFAF0F44528F2EFCA2578D40013CA06&0&July%202011&22.07.2011&Previous
data/CED_2011_AUST.zip  
# The first way is great during development as the step will get cached.  
# The second way is great for building on Docker Hub  
RUN service postgresql start; echo "INSERT INTO mapit_country (code, name)
VALUES ('AU', 'Australia');" | su -l -c "psql mapit" mapit  
  
RUN service postgresql start; su -l -c "/var/www/mapit/mapit/manage.py
mapit_generation_create --desc='Initial import' --commit" mapit  
RUN service postgresql start; su -l -c "/var/www/mapit/mapit/manage.py
mapit_generation_activate --commit" mapit  
  
ADD import.sh /import.sh  
RUN chmod +x /import.sh  
  
RUN /import.sh LGA_2011_AUST LGA 'Local Government Area' LGA_NAME11  
RUN /import.sh SED_2011_AUST SED 'State Electoral Division' SED_NAME  
RUN /import.sh POA_2011_AUST POA 'Postal Area' POA_CODE  
RUN /import.sh COM20111216_ELB_region CED 'Commonwealth Electoral Division'
ELECT_DIV  
#RUN /import.sh CED_2011_AUST CED 'Commonwealth Electoral Division' CED_NAME  
RUN /import.sh STE11aAust STE 'State and Territories' STATE_NAME  
  
ADD copyright.html /var/www/mapit/mapit/mapit/templates/mapit/copyright.html  
ADD country.html /var/www/mapit/mapit/mapit/templates/mapit/country.html  
  
RUN rm -rf /data  
  
# TODO: Make mapit handle areas with numeric names  
# TODO: Look for more authoritive sources for electoral boundaries, LGAs  
# TODO: Include Aborginal Areas  
# TODO: Include Suburbs  
# TODO: Include Council Wards?  
# Victorian Council Ward & State Electoral Division Boundaries:
https://www.vec.vic.gov.au/publications/publications-maps.html  
# South Australian LGAs: http://dpti.sa.gov.au/open_data_portal  

