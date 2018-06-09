# intel-mkl  
FROM takaomag/base:2017.01.16.05.02  
ENV \  
X_DOCKER_REPO_NAME=intel-mkl  
  
RUN \  
echo "2016-05-06-1" > /dev/null && \  
export TERM=dumb && \  
export LANG='en_US.UTF-8' && \  
source /opt/local/bin/x-set-shell-fonts-env.sh && \  
echo -e "${FONT_INFO}[INFO] Update package database${FONT_DEFAULT}" && \  
reflector --latest 100 --verbose --sort score --save /etc/pacman.d/mirrorlist
&& \  
sudo -u nobody yaourt -Syy && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Update package database${FONT_DEFAULT}" && \  
echo -e "${FONT_INFO}[INFO] Refresh package developer keys${FONT_DEFAULT}" &&
\  
pacman-key --refresh-keys && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Refresh package developer
keys${FONT_DEFAULT}" && \  
REQUIRED_PACKAGES=("gcc-fortran") && \  
if grep '^vendor_id' /proc/cpuinfo | head -1 | grep -i intel;then\  
export X_IS_INTEL=1 && REQUIRED_PACKAGES+=("intel-mkl");\  
else\  
export X_IS_INTEL=0;\  
fi && \  
# REQUIRED_PACKAGES=("gcc-fortran" "atlas-lapack-base") && \  
# REQUIRED_PACKAGES=("gcc-fortran" "atlas-lapack") && \  
echo -e "${FONT_INFO}[INFO] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
sudo -u nobody yaourt -S --needed --noconfirm --noprogressbar
"${REQUIRED_PACKAGES[@]}" && \  
if [[ "${X_IS_INTEL}" = '1' ]];then\  
mkdir /opt/intel/mkl/lib_sym && \  
cd /opt/intel/mkl/lib_sym && \  
ln -sf ../lib/intel64/libmkl_rt.so libblas.so && \  
ln -sf ../lib/intel64/libmkl_rt.so libblas.so.3 && \  
ln -sf ../lib/intel64/libmkl_rt.so liblapack.so && \  
ln -sf ../lib/intel64/libmkl_rt.so liblapack.so.3 && \  
echo '/opt/intel/mkl/lib_sym' > /opt/intel/mkl/x-blas.ld.so.conf && \  
install --owner=root --group=root --mode=0644 /opt/intel/mkl/x-blas.ld.so.conf
/etc/ld.so.conf.d/x-intel-mkl-comp-blas.ld.so.conf && \  
ldconfig; \  
fi && \  
echo -e "${FONT_SUCCESS}[SUCCESS] Install required packages
[${REQUIRED_PACKAGES[@]}]${FONT_DEFAULT}" && \  
/opt/local/bin/x-archlinux-remove-unnecessary-files.sh && \  
# pacman-optimize && \  
rm -f /etc/machine-id  
  

