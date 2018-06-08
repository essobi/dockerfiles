FROM tsutomu7/ubuntu-essential  
  
ENV USER=scientist HOME=/home/scientist \  
PATH=/opt/conda/bin:$PATH \  
LANG=C.UTF-8 \  
DEBIAN_FRONTEND=noninteractive \  
MINICONDA=Miniconda3-latest-Linux-x86_64.sh  
ADD nb.tgz $HOME/.jupyter/nbconfig/  
COPY jupyter_notebook_config.py $HOME/.jupyter/  
COPY generic.diff utils.diff pdfdoc.diff /tmp/  
RUN export uid=1000 gid=1000 pswd=scientist && \  
apt-get update --fix-missing && apt-get install -y --no-install-recommends
sudo \  
libglib2.0-0 libxext6 libsm6 libxrender1 tzdata busybox wget fonts-ipaexfont
&& \  
groupadd -g $gid $USER && \  
useradd -g $USER -G sudo -m -s /bin/bash $USER && \  
echo "$USER:$pswd" | chpasswd && \  
mkdir -p $HOME/.local/share/jupyter && \  
mkdir -p /etc/sudoers.d && \  
echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER && \  
chmod 0440 /etc/sudoers.d/$USER && \  
/bin/busybox --install && \  
cp --remove-destination /usr/share/zoneinfo/Japan /etc/localtime && \  
apt-get --purge autoremove -y tzdata && \  
apt-get clean && \  
echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget -q --no-check-certificate \  
https://repo.continuum.io/miniconda/$MINICONDA && \  
bash /$MINICONDA -b -p /opt/conda && \  
conda update -y --all && \  
conda install -y nomkl networkx scikit-learn jupyter blist numexpr blaze \  
statsmodels ncurses seaborn dask flask markdown sympy psutil \  
more-itertools redis redis-py gunicorn coverage reportlab pivottablejs && \  
pip install --no-cache pulp pyjade pypdf2==1.26.0 \  
ortoolpy yapf pdfformfiller pdfrw jupyter_dashboards toml && \  
jupyter dashboards quick-setup --sys-prefix && \  
jupyter nbextension enable --py --sys-prefix widgetsnbextension && \  
#pip install --no-cache https://github.com/ipython-contrib/IPython-notebook-
extensions/archive/master.zip && \  
#sed -i '6,9d' $HOME/.jupyter/jupyter_nbconvert_config.json && \  
ln -s /usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf
/usr/share/fonts/ipaexg.ttf && \  
find /opt -name __pycache__ | xargs rm -r && \  
chown ${uid}:${gid} -R $HOME /opt/conda && \  
cd /opt/conda/lib/python3.6/site-packages/PyPDF2 && \  
patch generic.py < /tmp/generic.diff && \  
patch utils.py < /tmp/utils.diff && \  
cd /opt/conda/lib/python3.6/site-packages/reportlab/pdfbase && \  
patch pdfdoc.py < /tmp/pdfdoc.diff && \  
rm -rf /var/lib/apt/lists/* /$MINICONDA /opt/conda/pkgs/* /tmp/*.diff \  
/opt/conda/lib/python3.6/site-packages/pulp/solverdir/cbc/[ow]* \  
/opt/conda/lib/python3.6/site-packages/pulp/solverdir/cbc/linux/32  
USER $USER  
WORKDIR $HOME  
CMD ["/bin/bash"]  

