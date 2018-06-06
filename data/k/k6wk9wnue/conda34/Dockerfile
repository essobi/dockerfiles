FROM continuumio/anaconda3  
MAINTAINER Gage Renzi <gagerenzi@gmail.com>  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN mkdir /setup  
COPY ./requirements.txt /setup  
  
WORKDIR /opt  
RUN /bin/bash -c "conda update psutil && conda create -y -q -n py34 python=3.4
anaconda"  
RUN /bin/bash -c "source activate py34 && conda config --add channels conda-
forge && conda info"  
# RUN /bin/bash -c "source activate py34 && pip install -r
/setup/requirements.txt"  
# RUN /bin/bash -c "source activate py34 && python -m nltk.downloader -d
/usr/local/share/nltk_data stopwords"  
CMD [ "/bin/bash -c -c \"source activate py34\"" ]

