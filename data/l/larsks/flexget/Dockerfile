FROM larsks/alpine-s6  
  
RUN apk add \  
ca-certificates \  
python \  
py-pip \  
py-feedparser \  
py-yaml \  
py-markupsafe \  
py-flask \  
py-itsdangerous \  
py-tz \  
py-six  
  
RUN pip install -U pip  
RUN pip install flexget  
  
COPY flexget.cron /etc/periodic/hourly/flexget  
COPY services /services  

