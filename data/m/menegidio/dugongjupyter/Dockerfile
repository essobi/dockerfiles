FROM dugong/dugong  
MAINTAINER Fabiano Menegidio  
  
USER root  
  
ENV NB_UID 1000  
ENV NB_USER dugong  
  
COPY .config/start.sh /usr/local/bin/  
COPY .config/start-notebook.sh /usr/local/bin/  
COPY .config/start-singleuser.sh /usr/local/bin/  
COPY .config/jupyter_notebook_config.py $HOME/.jupyter/  
  
RUN apt-get update && apt-get install -y --allow-unauthenticated fonts-
liberation \  
&& apt-get autoremove -y && apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& chmod +x /usr/local/bin/start.sh \  
&& chmod +x /usr/local/bin/start-notebook.sh \  
&& chmod +x /usr/local/bin/start-singleuser.sh \  
&& chown -R dugong:dugong $HOME  
  
USER dugong  
  
RUN echo "cacert=/etc/ssl/certs/ca-certificates.crt" > $HOME/.curlrc \  
&& ~/.conda2/bin/conda config --system --prepend channels conda-forge \  
&& ~/.conda2/bin/conda config --system --set auto_update_conda false \  
&& ~/.conda2/bin/conda config --system --set show_channel_urls true \  
&& ~/.conda2/bin/conda update --all \  
&& ~/.conda2/bin/conda install --quiet --yes \  
'notebook' \  
'ipykernel' \  
&& ~/.conda2/bin/conda clean -tipsy  
  
USER root  
EXPOSE 8888  
EXPOSE 22  
VOLUME ["/data", "/config"]  
RUN chown -R dugong:dugong /data && \  
chown -R dugong:dugong /config  
  
WORKDIR /data  
  
CMD ["start-notebook.sh"]  
  
USER dugong  

