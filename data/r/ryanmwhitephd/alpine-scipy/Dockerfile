FROM ryanmwhitephd/alpine-base:73bdef0  
  
MAINTAINER Ryan White <ryan.white4@canada.ca>  
  
RUN pip install --upgrade pip  
  
RUN pip install numpy && \  
pip install pandas && \  
pip install scipy  
  
RUN pip install cython  
  
RUN apk add --update freetype-dev \  
libpng && rm -rf /var/cache/apk/*  
  
RUN pip install ipython && \  
pip install matplotlib && \  
pip install seaborn  
  
RUN pip install scikit-learn && \  
pip install statsmodels  
  

