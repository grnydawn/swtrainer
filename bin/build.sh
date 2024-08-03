#!/bin/bash

SWT_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

source ${SWT_HOME}/bin/env.sh

export TEST_MPI_COMMAND="mpirun -n 1 "
BUILD_DIR=${SWT_HOME}/build

rm -rf ${BUILD_DIR}

PNETCDF_ROOT=/Users/8yk/opt/pnetcdf/1.13.0

cmake -DCMAKE_Fortran_COMPILER=mpif90 \
      -DFFLAGS="-O3 -ffree-line-length-none -I${PNETCDF_ROOT}/include"   \
      -DLDFLAGS="-L${PNETCDF_ROOT}/lib -lpnetcdf"                        \
      -DNX=100 \
      -DNZ=50  \
      -DSIM_TIME=100 \
      -DOUT_FREQ=200 \
      -B ${BUILD_DIR} \
      ${SWT_HOME}/cases/miniWeather

cd ${BUILD_DIR}

make -j8
