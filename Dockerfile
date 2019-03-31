FROM continuumio/miniconda3

# set up work directory.
WORKDIR /home/me/dev/

# copy necessary files.
COPY ./* ./

RUN pwd

RUN ls

# install packages.
RUN conda env create -f enviroment.yml

# run script.
CMD python my_script.py
