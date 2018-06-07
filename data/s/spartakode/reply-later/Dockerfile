FROM spartakode/py35:vanilla  
MAINTAINER Adnan Issadeen <adnan.issadeen@live.com>  
  
RUN apt-get update && apt-get install nginx software-properties-common python-
software-properties -y --force-yes  
RUN apt-add-repository ppa:git-core/ppa -y && apt-get update -y && apt-get
install git -y  
RUN pip3.5 install Flask python-crontab twitter-text-python  
RUN pip3.5 install git+https://github.com/tweepy/tweepy.git  
  
ADD prodnginxfile /etc/nginx/sites-available/pyapp  
RUN rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-
available/pyapp /etc/nginx/sites-enabled/pyapp  
  

