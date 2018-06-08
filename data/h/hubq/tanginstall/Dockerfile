FROM hubq/tanglabngssftw:latest  
  
RUN yum groupinstall -y 'Development Tools'  
  
RUN yum install -y git curl curl-devel gcc python python-devel zsh tar bzip2
gcc-c++ readline-devel gmp-devel gcc-gfortran cmake zlib zlib-devel mysql
mysql-devel libpng libpng12 libpng-devel libtiff libtiff-devel libjpeg
libjpeg-devel openssh-clients boost boost-devel  
  
#RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python
get-pip.py && pip install s3cmd  
#RUN pip install s3cmd  
#  
RUN mkdir software  
#  
#RUN wget -q http://166.111.152.116:13334/tangfuchou/install_packages.tar.bz2  
#  
WORKDIR /software  
##RUN touch abc.txt  
RUN tar -jxvf /install_packages.tar.bz2  
  
  
WORKDIR /software  
##RUN touch abc.txt  
RUN tar -jxvf /install_packages.tar.bz2  
#  
### R 3.2.0  
WORKDIR /software/install_packages/R-3.2.0  
RUN ./configure \--prefix=/opt/R \--with-x=no  
RUN make  
RUN make install  
WORKDIR /software/install_packages  
# anaconda  
RUN bash ./Anaconda-2.2.0-Linux-x86_64.sh -b -p /opt/conda  
#  
RUN yum install -y java  
  
# bedtools  
WORKDIR /software/install_packages/bedtools2/  
RUN make  
WORKDIR /software/install_packages/  
# bwa & samtools & tabix  
WORKDIR /software/install_packages/bwa-0.7.5a  
RUN make  
WORKDIR /software/install_packages/  
  
WORKDIR /software/install_packages/samtools-0.1.18  
RUN make  
WORKDIR /software/install_packages/  
#  
WORKDIR /software/install_packages/tabix-0.2.6  
RUN make  
WORKDIR /software/install_packages/  
#  
## MACS2  
ENV PATH /opt/conda/bin:$PATH  
ENV PYTHONPATH /opt/conda/lib/python2.7/site-packages/:$PYTHONPATH  
#  
WORKDIR /software/install_packages/MACS2-2.1.0.20150731  
RUN python setup_w_cython.py install  
WORKDIR /software/install_packages/  
#  
# pip install  
RUN pip install pysam==0.8.3 pybedtools==0.6.9  
RUN pip install -d . ngslib  
RUN pip install HTSeq==0.6.0 brewer2mpl svgwrite seaborn sklearn  
RUN conda install mysql-python  
#  
# jupyter  
#RUN conda install jupyter  
#ENV TINI_VERSION v0.6.0  
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
#RUN chmod +x /usr/bin/tini  
#ENTRYPOINT ["/usr/bin/tini", "--"]  
#EXPOSE 8888  
#RUN mkdir -p -m 700 /root/.jupyter/  
#RUN echo "c.NotebookApp.ip = '*'" >>
/root/.jupyter/jupyter_notebook_config.py  
##RUN jupyter notebook --port=8888 --no-browser --ip=0.0.0.0  
#CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN /software/install_packages/R-3.2.0/bin/Rscript -e
"install.packages('caTools')"  
RUN /software/install_packages/R-3.2.0/bin/Rscript -e
"install.packages('snow')"  
RUN /software/install_packages/R-3.2.0/bin/R CMD INSTALL
spp_rev/spp_1.10.1.tar.gz  
  
RUN adduser -g games analyzer  
RUN mkdir -p /home/analyzer/project  
RUN chown -R analyzer:games /home/analyzer/project  
  
RUN sed 's/source("functions-all-
clayton-12-13.r")/source("\/software\/install_packages\/idrCode\/functions-
all-clayton-12-13.r")/g' /software/install_packages/idrCode/batch-consistency-
analysis.r | \  
sed 's/"genome_table.txt"/args[8]/g' >tmp && mv tmp
/software/install_packages/idrCode/batch-consistency-analysis.r  
  
USER analyzer  
  
  
  
  
#RUN adduser -g games analyzer  
#USER analyzer  
ENV PATH /opt/conda/bin:$PATH  
ENV PYTHONPATH /opt/conda/lib/python2.7/site-packages/:$PYTHONPATH  
WORKDIR /home/analyzer  
RUN git clone https://github.com/huboqiang/my_zsh  
RUN cp -r my_zsh/.oh-my-zsh ./ && cp -r my_zsh/.vim ./ && cp my_zsh/.vimrc ./
&& cp my_zsh/.zshrc ./ && cp my_zsh/rmate ./  
#  
RUN echo ""  
RUN mkdir -p /home/analyzer/project /home/analyzer/module
/home/analyzer/database_RNA /home/analyzer/database_ChIP  
WORKDIR /home/analyzer/module  
ENV PYTHONPATH /home/analyzer/module/:$PYTHONPATH  
RUN git clone https://github.com/huboqiang/RNA_v2  
RUN sed
's/\/data\/Analysis\/huboqiang\/software\/anaconda\/bin\/python/\/opt\/conda\/bin\/python/g'
./RNA_v2/settings/projpath.py |\  
sed
's/\/data\/Analysis\/huboqiang\/lib\/local_perl\/bin\/perl/\/usr\/bin\/perl/g'
|\  
sed 's/\/data\/Analysis\/huboqiang\/software/\/software\/install_packages/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/Database_RNA_v2/\/home\/analyzer\/database_RNA/g'
|\  
sed 's/bowtie2-2.1.0/bowtie2-2.2.3/g' |\  
sed 's/bedtools-2.17.0/bedtools2/g' |\  
sed
's/\/software\/install_packages\/anaconda\/lib\/python2.7/\/opt\/conda\/lib\/python2.7/g'
|\  
sed 's/\/usr\/local\/bin/\/software\/install_packages\/tabix-0.2.6/g' |\  
sed 's/Bowtie\///g'>tmp &&\  
mv tmp ./RNA_v2/settings/projpath.py  
#  
  
RUN git clone https://github.com/huboqiang/ChIP  
RUN sed
's/\/data\/Analysis\/huboqiang\/software\/anaconda\/bin\/python/\/opt\/conda\/bin\/python/g'
./ChIP/settings/projpath.py |\  
sed
's/\/data\/Analysis\/huboqiang\/lib\/local_perl\/bin\/perl/\/usr\/bin\/perl/g'
|\  
sed 's/\/data\/Analysis\/huboqiang\/software/\/software\/install_packages/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/Database_ChIP_v2/\/home\/analyzer\/database_ChIP/g'
|\  
sed 's/bedtools-2.17.0/bedtools2/g' |\  
sed 's/MACS/MACS2-2.1.0.20150731/g' |\  
sed
's/\/software\/install_packages\/tabix/\/software\/install_packages\/tabix-0.2.6/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/bin\/bwa/\/software\/install_packages\/bwa-0.7.5a\/bwa/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/bin\/igvtools/\/software\/install_packages\/IGVTools\/igvtools/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/project\/human_sc\/chIp_analysis\/bin/\/home\/analyzer\/project\/ChIP\/bin/g'
|\  
sed 's/\/software\/install_packages\/study_broadMacsScripts\/idrCode\/batch-
consistency-analysis.r/\/software\/install_packages\/idrCode\/batch-
consistency-analysis.r/g' |\  
sed
's/\/home\/analyzer\/project\/ChIP\/bin/\/home\/analyzer\/module\/ChIP\/bin/g'
|\  
sed
's/\/data\/Analysis\/huboqiang\/bin\/Rscript/\/software\/install_packages\/R-3.2.0\/bin\/Rscript/g'
>tmp &&\  
mv tmp ./ChIP/settings/projpath.py  
  
RUN mkdir /home/analyzer/bin  
RUN cp /software/install_packages/R-3.2.0/bin/Rscript /home/analyzer/bin && \  
cp /software/install_packages/R-3.2.0/bin/R /home/analyzer/bin && \  
cp /software/install_packages/picard-tools-1.119/MarkDuplicates.jar
/home/analyzer/bin && \  
cp /software/install_packages/bwa-0.7.5a/bwa /home/analyzer/bin && \  
cp /software/install_packages/samtools-0.1.18/samtools /home/analyzer/bin && \  
cp /software/install_packages/MACS2-2.1.0.20150731/bin/macs2
/home/analyzer/bin && \  
cp /software/install_packages/bedtools2/bin/bedtools /home/analyzer/bin && \  
cp /software/install_packages/tabix-0.2.6/tabix /home/analyzer/bin && \  
cp /software/install_packages/tabix-0.2.6/bgzip /home/analyzer/bin && \  
cp /software/install_packages/bowtie2-2.2.3/bowtie2* /home/analyzer/bin  
  
WORKDIR /home/analyzer/  
ADD ./src/run_sample.sh /home/analyzer/run_sample.sh  
  
ENV PATH /home/analyzer/bin:$PATH  
  
WORKDIR /home/analyzer/project  
  
CMD ["sh", "/home/analyzer/run_sample.sh"]  

