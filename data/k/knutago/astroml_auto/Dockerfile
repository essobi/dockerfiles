FROM debian:stretch  
MAINTAINER Upendra Devisetty <upendra@cyverse.org>  
LABEL version="1.0" description="This image is for astroML"  
  
# The base image is minimal with very few software packages. We  
# udpate apt and install python-pip with recommanded packages here.  
RUN apt-get -qq update &&\  
apt-get install -y python-pip &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Next, we install astroML's dependencies and astroML itself using pip.  
RUN pip install numpy scipy scikit-learn matplotlib astropy &&\  
pip install astroML astroML_addons  
  
# Change the default work directory to "/root" inside the container.  
WORKDIR /root  
  
# Install Jupyter and other visualization packages  
RUN pip install jupyter ipywidgets &&\  
jupyter nbextension enable \--py --sys-prefix widgetsnbextension  
  
COPY plot_spectrum_sum_of_norms.py /usr/bin  
COPY run.sh /usr/bin  
RUN chmod +x /usr/bin/plot_spectrum_sum_of_norms.py  
RUN chmod +x /usr/bin/run.sh  
ENTRYPOINT ["run.sh"]  

