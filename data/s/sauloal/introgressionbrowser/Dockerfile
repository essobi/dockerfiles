#BUILD: docker build --rm -t sauloal/introgressionbrowser .  
#RUN : docker stop ibrowser; docker rm ibrowser; docker run --detach=true
--name ibrowser --publish=10000:10000 --volume
$PWD/data:/var/www/ibrowser/data sauloal/introgressionbrowser  
#START: docker start ibrowser  
#LOGS : docker logs ibrowser  
#  
#--security-context apparmor:unconfine  
# --security-context  
FROM sauloal/introgressionbrowser_runtime  
  
RUN cd /var/www && git clone
https://github.com/sauloal/introgressionbrowser.git ibrowser && ls ibrowser  
  
RUN cd /var/www/ibrowser && pip install --requirement requirements.txt  
  
VOLUME /var/www/ibrowser/data  
#VOLUME /var/log/apache2/access.log  
#VOLUME /var/log/apache2/error.log  
WORKDIR /var/www/ibrowser  
  
CMD /var/www/ibrowser/reloader.py /var/www/ibrowser/ibrowser.py
/var/www/ibrowser/data  

