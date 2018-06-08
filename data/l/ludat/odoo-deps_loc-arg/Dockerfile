FROM ludat/odoo-deps:8.0  
MAINTAINER lucas6246@gmail.com  
  
# Maybe someday I'll need this  
# RUN export LANG=en_US.UTF-8 \  
# && apt-get update && apt-get install -y \  
ADD requirements.txt /more_requirements.txt  
RUN pip install -r /more_requirements.txt && \  
echo "#More requirements for odoo localization argentina" >> requirements.txt
&& \  
cat more_requirements.txt >> requirements.txt  

