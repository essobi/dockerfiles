####  
# Basics  
####  
FROM continuumio/anaconda  
  
LABEL maintainer=rwalters@broadinstitute.org  
  
# not in base image  
RUN apt-get install -y unzip  
  
# download lastest LDSC  
WORKDIR /home  
RUN git clone https://github.com/bulik/ldsc.git  
  
# put ldsc on path  
ENV PATH /home/ldsc:$PATH  
  
  
###  
# download and unpack LDSC reference files  
###  
  
WORKDIR /home/ld_ref_panel/  
  
# core  
ADD http://data.broadinstitute.org/alkesgroup/LDSCORE/eur_w_ld_chr.tar.bz2 ./  
RUN tar -xjf eur_w_ld_chr.tar.bz2 && rm eur_w_ld_chr.tar.bz2  
ADD http://data.broadinstitute.org/alkesgroup/LDSCORE/w_hm3.snplist.bz2 ./  
RUN bzip2 -d /home/ld_ref_panel/w_hm3.snplist.bz2  
  
# baseline paritioning  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/1000G_Phase3_baseline_ldscores.tgz
./  
# ADD http://data.broadinstitute.org/alkesgroup/LDSCORE/1000G_Phase3_frq.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/1000G_Phase3_weights_hm3_no_MHC.tgz
./  
# RUN tar -zxvf /home/ld_ref_panel/1000G_Phase3_baseline_ldscores.tgz && \  
# tar -zxvf /home/ld_ref_panel/1000G_Phase3_frq.tgz && \  
# tar -zxvf /home/ld_ref_panel/1000G_Phase3_weights_hm3_no_MHC.tgz  
  
# tissue groups  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/1000G_Phase3_cell_type_groups.tgz
./  
# RUN tar -zxvf /home/ld_ref_panel/1000G_Phase3_cell_type_groups.tgz  
  
# continuous  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/1000G_Phase3_baselineLD_ldscores.tgz
./  
# RUN tar -zxvf /home/ld_ref_panel/1000G_Phase3_baselineLD_ldscores.tgz  
  
# cell-type specific  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Cahoy.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Cahoy_1000Gv3.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Franke.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Franke_1000Gv3.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/GTEx.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/GTEx_1000Gv3.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/GTEx_brain.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/GTEx_brain_1000Gv3.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/ImmGen.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/ImmGen_1000Gv3.tgz
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Roadmap.ldcts
./  
# ADD
http://data.broadinstitute.org/alkesgroup/LDSCORE/LDSC_SEG_ldscores/Roadmap_1000Gv3.tgz
./  
# RUN tar -zxvf /home/ld_ref_panel/Cahoy_1000Gv3.tgz && \  
# tar -zxvf /home/ld_ref_panel/Franke_1000Gv3.tgz && \  
# tar -zxvf /home/ld_ref_panel/GTEx_1000Gv3.tgz && \  
# tar -zxvf /home/ld_ref_panel/GTEx_brain_1000Gv3.tgz && \  
# tar -zxvf /home/ld_ref_panel/ImmGen_1000Gv3.tgz && \  
# tar -zxvf /home/ld_ref_panel/Roadmap_1000Gv3.tgz  

