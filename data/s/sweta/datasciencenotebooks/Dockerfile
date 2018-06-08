  
FROM ubuntu:14.04  
USER root  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
python-pip --upgrade python-pip  
  
RUN pip install --upgrade pip  
  
# RUN pip install --upgrade pip  
RUN sudo apt-get install python-requests  
RUN pip install beautifulSoup  
RUN pip install bs4  
RUN pip install pandas  
RUN pip install zip  
RUN pip install boto  
RUN pip install tinys3  
# RUN pip install sys  
# install py3  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
# install python 3  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
pkg-config \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip  
  
# install additional python packages  
RUN pip3 install ipython  
RUN pip3 install jupyter  
RUN pip3 install pandas  
RUN pip3 install scikit-learn  
#RUN pip install rpy2  
# configure console  
RUN echo 'alias ll="ls --color=auto -lA"' >> /root/.bashrc \  
&& echo '"\e[5~": history-search-backward' >> /root/.inputrc \  
&& echo '"\e[6~": history-search-forward' >> /root/.inputrc  
# default password: keras  
ENV PASSWD='sha1:98b767162d34:8da1bc3c75a0f29145769edc977375a373407824'  
# dump package lists  
RUN dpkg-query -l > /dpkg-query-l.txt \  
&& pip2 freeze > /pip2-freeze.txt \  
&& pip3 freeze > /pip3-freeze.txt  
  
# for jupyter  
EXPOSE 8888  
COPY . /srv  
# Add a notebook profile.  
# ADD /DataScienceNotebooks/Data Files/ /srv/n2/  
# RUN mkdir -p -m 700 /root/.jupyter/ && \  
# echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/ClassData_Script.py  
# RUN mkdir /srv/n3  
# COPY /C/Users/sweta/PythonApp/ClassData_Script.py
/srv/notebooks/ClassData_Script.py  
WORKDIR /srv/  
  
# RUN mkdir /srv/nb1/  
CMD /bin/bash -c 'jupyter notebook --no-browser --ip=*
--NotebookApp.password="$PASSWD" "$@"'  
  
# CMD /bin/bash -c 'jupyter notebook --no-browser --ip=*
--NotebookApp.password="keras" "$@"'  

