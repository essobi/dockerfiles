#  
# 2017 © Headcount Solutions Ltd.  
# See 'LICENCE.md' in the project root for more information.  
#  
FROM frolvlad/alpine-python2  
MAINTAINER Neil Hyland <neil.hyland@bimandscan.com>  
  
# Setup environment:  
RUN apk update --no-cache && \  
apk upgrade --no-cache && \  
apk add --no-cache git && \  
pip install -U pyparsing && \  
mkdir -p /ifcopenshell && \  
git clone "https://github.com/IfcOpenShell/IfcOpenShell.git" /ifcopenshell  
  
# Setup generator:  
WORKDIR /ifcopenshell/src/ifcexpressparser  
COPY ./scripts/GenerateSchemas.sh .  
  
RUN chmod +x ./GenerateSchemas.sh && \  
python bootstrap.py express.bnf > express_parser.py  
  
VOLUME /schemas  
VOLUME /generated  
  
ENTRYPOINT ["/bin/sh", "./GenerateSchemas.sh"]  
  

