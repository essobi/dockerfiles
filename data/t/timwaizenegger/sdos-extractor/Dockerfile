# Project MCM  
#  
# Copyright (C) <2015-2017> Tim Waizenegger, <University of Stuttgart>  
#  
# This software may be modified and distributed under the terms  
# of the MIT license. See the LICENSE file for details.  
FROM python:3.6  
MAINTAINER Tim Waizenegger <tim.waizenegger@ipvs.uni-stuttgart.de>  
  
RUN git clone https://github.com/sdos/metadata-extractor.git  
WORKDIR metadata-extractor  
RUN pip install -r requirements.txt  
RUN cp mcm/metadataExtractor/configuration.example.py
mcm/metadataExtractor/configuration.py  
  
COPY extractor.sh /  
  
ENTRYPOINT ["/extractor.sh"]

