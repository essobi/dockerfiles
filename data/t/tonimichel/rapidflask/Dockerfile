From tonimichel/pythonbase  
ONBUILD ENV LANG c.utf8  
ONBUILD ENV LC_ALL c.utf8  
ONBUILD ENV LANGUAGE en_US.utf8  
ONBUILD RUN pip install pip --upgrade  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install --upgrade --no-cache-dir -r
/usr/src/app/requirements.txt  
#ONBUILD RUN rm /usr/src/app/requirements.txt  

