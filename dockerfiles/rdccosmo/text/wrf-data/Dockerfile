FROM rdccosmo/wrf-arwpost
RUN mkdir /home/wrf/data
RUN sed -i "s/geog_data_path = .*/geog_data_path = '\/home\/wrf\/data\/'/" /home/wrf/Build_WRF/LIBRARIES/WPS/namelist.wps
VOLUME /home/wrf/data
