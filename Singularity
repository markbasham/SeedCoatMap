Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./
%post

# set up work directory.
cd /home/me/dev/

# copy necessary files.

# install packages.
conda env create -f enviroment.yml

#Activate the enviroment
/bin/bash -c "source activate main"

# run script.
%runscript
exec /bin/bash "$@"
